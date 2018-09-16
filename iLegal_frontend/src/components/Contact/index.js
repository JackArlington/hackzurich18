import React from 'react';
import { Card, Title, P, Subtitle } from './style';

class Contact extends React.Component {
	// renderCases = (cases) => {
	// 	const casesDON = [];
	// 	cases.forEach(case => {
	// 		console.log(case)
	// 	});

	// 	return casesDON;
	// }

	render() {
		const { details } = this.props;
		const pastCases = details.pastCases.map(a => <li>{a}</li>);
		const remarks = details.remarks.map(a => <li>{a}</li>);

		return (
			<Card>
				<Title>{details.firstname + ' ' + details.surname}</Title>
				<P>{details.company}</P>
				<div style={{ display: 'flex', justifyContent: 'space-between' }}>
					<Subtitle>
						{pastCases && <React.Fragment><span>PAST CASES</span><ul>{pastCases}</ul></React.Fragment>}
					</Subtitle>
				</div>
				<div style={{ display: 'flex', justifyContent: 'space-between' }}>
					<Subtitle>
						{remarks && <React.Fragment><span>REMARKS</span><ul>{remarks}</ul></React.Fragment>}
					</Subtitle>
				</div>
			</Card>
		)
	}
}

export default Contact;
