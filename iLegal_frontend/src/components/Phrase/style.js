import styled, {
  keyframes
} from 'styled-components';

export const Wrapper = styled.div `
  position: relative;
  z-index: 1;
`;

export const Bound = styled.div`
	width: 90%;
	height: 72vh;
  margin: 0 auto;
  max-width: 436px;
  min-height: 200px;
`;

export const Text = styled.div `
	line-height: 3rem;
	opacity: 0.6;
	will-change: transform, opacity;
  color: snow;
  font-size: 2rem;
  overflow: hidden;
  padding: 12px;
  position: relative;
  transform: translateZ(0);
`;

export const Title = styled(Text)`
	font-size: 2.4rem;
	font-weight: 700;
	opacity: 1;
	border-bottom: 1px solid #eaeaea;
`;
