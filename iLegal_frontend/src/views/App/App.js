  import React from 'react';

  import Phrase from '../../components/Phrase';
  import Contact from '../../components/Contact';
  import { ControlButton, ButtonContainer, Logo } from './style';

  import Mic from '../../assets/mic.svg';
  import StopCircle from '../../assets/stop-circle.svg';
  import { API } from '../../api';

  const KEY = '0bc834e91166449296f4a84d38c6c4e0';

  class App extends React.Component {
    constructor(props) {
      super(props)

      this.state = {
        view: 'default',
        title: `iLegal`,
        details: {},
        isRecording: false,
        phrase: `A digital assistant to leverage the lawyer client interaction`
      }
    }

    // On document load resolve the SDK dependency
    Initialize = (onComplete) => {
      if (!!window.SDK) {
        console.log('Initialized!');
        // document.getElementById('warning').style.display = 'none';
        // document.getElementById('content').style.display = 'block';
        // this.onComplete(window.SDK);
      }
    }

    // Setup the recognizer
    RecognizerSetup = (SDK) => {
      var recognizerConfig = new SDK.RecognizerConfig(
        new SDK.SpeechConfig(
          new SDK.Context(
            new SDK.OS(navigator.userAgent, "Browser", null),
            new SDK.Device("SpeechSample", "SpeechSample", "1.0.00000"))),
        SDK.RecognitionMode.Conversation,
        "en-US", // Supported languages are specific to each recognition mode. Refer to docs.
        "Simple"); // SDK.SpeechResultFormat.Simple (Options - Simple/Detailed)


      var useTokenAuth = false;

      var authentication = function () {
        if (!useTokenAuth)
          return new window.SDK.CognitiveSubscriptionKeyAuthentication(KEY);

        var callback = function () {
          var tokenDeferral = new window.SDK.Deferred();
          try {
            var xhr = new (XMLHttpRequest)('MSXML2.XMLHTTP.3.0');
            xhr.open('GET', '/token', 1);
            xhr.onload = function () {
              if (xhr.status === 200) {
                tokenDeferral.Resolve(xhr.responseText);
              } else {
                tokenDeferral.Reject('Issue token request failed.');
              }
            };
            xhr.send();
          } catch (e) {
            window.console && console.log(e);
            tokenDeferral.Reject(e.message);
          }
          return tokenDeferral.Promise();
        }

        return new window.SDK.CognitiveTokenAuthentication(callback, callback);
      }();

      return window.SDK.CreateRecognizer(recognizerConfig, authentication);
    }

    // Start the recognition
    RecognizerStart = (SDK, recognizer) => {
      recognizer.Recognize((event) => {
        /*
        Alternative syntax for typescript devs.
        if (event instanceof SDK.RecognitionTriggeredEvent)
        */
        switch (event.Name) {
          case "RecognitionTriggeredEvent":
            this.UpdateStatus("Initializing");
            break;
          case "ListeningStartedEvent":
            this.UpdateStatus("Listening");
            break;
          case "RecognitionStartedEvent":
            this.UpdateStatus("Listening_Recognizing");
            break;
          case "SpeechStartDetectedEvent":
            this.UpdateStatus("Listening_DetectedSpeech_Recognizing");
            console.log(JSON.stringify(event.Result)); // check console for other information in result
            break;
          case "SpeechHypothesisEvent":
          case "SpeechFragmentEvent":
            console.log(JSON.stringify(event.Result)); // check console for other information in result
            break;
          case "SpeechEndDetectedEvent":
            this.OnSpeechEndDetected();
            this.UpdateStatus("Processing_Adding_Final_Touches");
            console.log(JSON.stringify(event.Result)); // check console for other information in result
            break;
          case "SpeechSimplePhraseEvent":
            this.UpdateRecognizedPhrase(JSON.stringify(event.Result, null, 3));
            break;
          case "SpeechDetailedPhraseEvent":
            this.UpdateRecognizedPhrase(JSON.stringify(event.Result, null, 3));
            break;
          case "RecognitionEndedEvent":
            // this.OnComplete();
            this.UpdateStatus("Idle");
            console.log(JSON.stringify(event)); // Debug information
            break;
          default:
            console.log(JSON.stringify(event)); // Debug information
        }
      })
        .On(() => {
          // The request succeeded. Nothing to do here.
        },
          (error) => {
            console.error(error);
          });
    }

    // Stop the Recognition.
    RecognizerStop = (SDK, recognizer) => {
      // recognizer.AudioSource.Detach(audioNodeId) can be also used here. (audioNodeId is part of ListeningStartedEvent)
      this.recognizer.AudioSource.TurnOff();
    }

    UpdateStatus = status => {
      console.log('status updated');
    }

    componentDidMount = () => {
      document.addEventListener("DOMContentLoaded", () => {
        const createBtn = document.getElementById("createBtn");
        const startBtn = document.getElementById("startBtn");

        startBtn.addEventListener("click", () => {
          if (KEY == "" || KEY == "YOUR_BING_SPEECH_API_KEY") {
            alert("Please enter your Bing Speech subscription key!");
            return;
          }

          if (!this.recognizer) {
            this.Setup();
          }

          this.RecognizerStart(window.SDK, this.recognizer);
          startBtn.disabled = true;
        });

        // this.RecognizerStop(window.SDK, recognizer);

        this.Initialize(function (speechSdk) {
          window.SDK = speechSdk;
        });
      });
    }

    Setup = () => {
      if (this.recognizer != null) {
        this.RecognizerStop(window.SDK, this.recognizer);
      }
      this.recognizer = this.RecognizerSetup(window.SDK);
    }

    UpdateRecognizedPhrase = async (json) => {
      const phrase = JSON.parse(json);


      if (phrase.RecognitionStatus === "Success") {
        const {
          data
        } = await API.getCatchphrase(json);


        if (data.hasOwnProperty('firstname')) {
          this.setState({
            view: 'contact',
            details: data,
            phrase: 'A digital assistant to leverage the lawyer client interaction',
            title: 'iLegal',
          });
        } else if (data.hasOwnProperty('case_title') && data.hasOwnProperty('relevant_catchphrase')) {
          this.setState({
            view: 'phrase',
            detail: {},
            phrase: data.case_title[0],
            title: data.relevant_catchphrase,
          });
				}

				// else {
        //   this.setState({
        //     view: 'default',
        //     details: {},
        //     phrase: 'A digital assistant to leverage the lawyer client interaction',
        //     title: 'iLegal',
        //   });
        // }

        // this.setState({ phrase: phrase.DisplayText + "\n" });
      }
    }

    OnComplete = () => {
      // console.log('completed!')
      // startBtn.disabled = false;
    }

    handleButtonClick = () => {
      this.setState({ isRecording: !this.state.isRecording });
    }

    render() {
      const { isRecording, phrase, title, details, view } = this.state;
      const show = {
        Phrase:  view === 'default' || view === 'phrase',
        Contact: view === 'contact'
      }

      return (
        <div className="App">
          <Logo>
            <div style={{ backgroundColor: '#00FFCE', color: '#001417', padding: '4px 8px', borderRadius: 2 }}>
              iLegal
            </div>
          </Logo>
          {show.Phrase && <Phrase title={title} phrase={phrase} isRecording={isRecording} />}
          {show.Contact && <Contact details={details} />}
          <ButtonContainer id="startBtn">
            <p>Built by <span style={{fontWeight: 600}}>iLegal Team</span> for <span style={{fontWeight: 600}}>HackZürich</span>🇨🇭</p>
            <ControlButton type="button" onClick={this.handleButtonClick} isRecording={isRecording}>
              <img style={{ height: 24, width: 24 }} src={isRecording ? StopCircle : Mic} />
            </ControlButton>
          </ButtonContainer>
        </div>
      );
    }
  }

  export default App;
