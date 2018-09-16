import React from 'react';

import { Wrapper, Text, Title, Bound } from './style.js';

const Phrase = ({ title, isRecording, phrase }) => (
  <Wrapper>
		<Bound>
			<Title isSmall={title.length > 80}>
				{isRecording && title === 'iLegal' ? `Recording` : title}
			</Title>
			<Text id="phraseDiv" isSmall={phrase.length > 150}>
				{isRecording && title === 'iLegal' ? `Listening to conversation and looking for context...` : phrase}
			</Text>
		</Bound>
  </Wrapper>
);

export default Phrase;
