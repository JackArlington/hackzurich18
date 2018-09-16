import React from 'react';

import { Wrapper, Text, Title, Bound } from './style.js';

const Phrase = ({ title, isRecording, phrase }) => (
  <Wrapper>
		<Bound>
			<Title>
				{isRecording ? `Recording conversation` : title}
			</Title>
			<Text id="phraseDiv">
				{isRecording ? `Listening to conversation and looking for context...` : phrase}
			</Text>
		</Bound>
  </Wrapper>
);

export default Phrase;
