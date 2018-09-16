# hackzurich18

## Get it up and running
### Backend:
```
cd iLegal_backend
```
```
python -m pip install -r requirements.txt
```
```
./runserver.sh
```
### Frontend:
```
cd iLegal_frontend
```
```
yarn
```
```
yarn start
```

## Inspiration
Since the invention of fax, the communication between lawyers and their clients has hardly changed. 
The direct interaction with the client is crucial. During this interaction the lawyer has no assistance and needs a vast amount of information about the context, past cases and customer information.
We aim to give the lawyer real time information about the current case, the client and relevant past cases. At the same time iLegal records and transcribes the conversation between the lawyer and the client.
Thanks to iLegal the lawyer does need less meetings with the client because he has access to insights of his knowledge base in real time during the meeting. Also, he does not need any transcription afterwards. Hence the lawyer saves time and cost on a daily basis.

## What it does
iLegal supports the lawyer in the direct communication with the mandate. 

## How we built it
We use a voice assistant web app to gather the content of meetings and to provide real time insights to the lawyer.
The real time information is served by a server backend. As a proof of concept the backend is based on a huge database of Australian supreme court cases. We use natural language processing to identify relevant concepts in the transcribed text of the meeting as well as the data in the database. We then use Jaccard similarity to detect the most relevant cases which are then submitted to the frontend.
To identify the customer, our system keeps track of clients and provides the lawyer with relevant information about the user such as interests, former cases, remarks from past communication etc.


## Challenges we ran into
The provided data set was not adequate because of the German language and the generality of the described cases. Therefore we needed to invest time to find a suitable alternative.
The google, amazon and IBM watson speech to text APIs turned out to be not usable. We were happy to discover the Microsoft Azure solution.

## Accomplishments that we're proud of
The great frontend, the user identification, past case prediction.
We are convinced that our system will revolutionize the way lawyers work. The communication via email is not necessary anymore.

## What we learned
See challenges

## What's next for iLegal
The MVP of this hackathon shows the enormous potential of iLegal. The disruptive change in how lawyers communicate with their clients has the power to transform an entire business sector. 
We aim to get feedback from lawyers and improve the current prototype.

---
Backend magic by:
@JackArlington and @pjkfc

Frontend love by:
@apollonian11
