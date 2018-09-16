import styled from 'styled-components';

export const ControlButton = styled.button `
		margin-top: -124px;
    background-color: ${props => props.isRecording ? '#FF0078' : '#00FFCE'};
    border-radius: 32px;
    border: 1px solid rgb(0, 18, 21, 0.21);
    border: none;
    box-shadow: 0 4px 12px 4px rgb(0, 18, 21, 0.2);
		height: 64px;
		max-width: 436px;
    min-height: 64px;
    min-width: 64px;
    outline: none;
    width	: 64px;

    :hover {
				cursor: pointer;
				transform: translateY(-2px);
				transition: transform 200ms ease-in-out;
		}

    @media (max-width: 720px) {
			width: 100%;
			margin-top: -56px;
		}
`;

export const ButtonContainer = styled.div `
		padding: 24px 72px;
    align-items: center;
    bottom: 0;
    display: flex;
    height: 128px;
    justify-content: space-between;
    position: fixed;
		width: 100%;
		background-color: rgb(0, 255, 216, 0.1);

    @media (max-width: 720px) {
			padding: 24px 36px;
			flex-direction: column-reverse;
			width: 100%;
        /* justify-content: center; */
    }
`;

export const Logo = styled.span`
	align-items: center;
	display: flex;
	font-family: 'Sweet Sans Pro';
	font-size: 1rem;
	height: 72px;
	justify-content: center;
	width: 100%;

	@media (max-width: 720px) {
		justify-content: flex-start;
	}
`;
