import styled from 'styled-components';

export const Card = styled.div`
	background: #f2f2f2;
	border-radius: 8px;
	display: flex;
	flex-direction: column;
	margin: 12px auto;
	max-width: 470px;
	padding: 12px 20px;
	width: calc(100% - 24px);
`;

export const Title = styled.h1`
	font-size: 28px;
	font-weight: 700;
	line-height: 40px;
	color: #373737;
`;

export const P = styled.p `
	font-size: 18px;
	font-weight: 400;
	line-height: 22px;
	margin-top: 20px;
	color: #646464;
`;

export const Subtitle = styled.span`
	color: #757D8E;
	font-size: 17px;
	font-weight: 400;
	line-height: 24px;
`;
