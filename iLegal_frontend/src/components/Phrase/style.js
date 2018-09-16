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
	line-height: ${props => props.isSmall ? `1.5rem` : `2.8rem`};	opacity: 0.6;
	will-change: transform, opacity;
  color: snow;
	font-size: ${props => props.isSmall ? `1rem` : `2rem`};  overflow: hidden;
  padding: 12px;
  position: relative;
  transform: translateZ(0);
`;

export const Title = styled(Text)`
	border-bottom: 1px solid #eaeaea;
	font-size: ${props => props.isSmall ? `1.2rem` : `2.4rem`};
	font-weight: 700;
	line-height: ${props => props.isSmall ? `1.6rem` : `2.8rem`};
	opacity: 1;
	text-transform: capitalize;
`;
