import { useState } from 'react';
import { Navigate, useLocation } from 'react-router-dom';
import { Form, convertFormDataToJSON } from '../Globals/Form';
import '../css/master.css';
import airplane from '../assets/airplane.gif';

function FlightCard(props) {
	const [redirect, setRedirect] = useState({ to: '', state: {}, replace: false });
	const [limitParams, setLimitParams] = useState([
		{ label: 'Max Iterations', type: 'number', value: 25, min: 0 },
		{ label: 'Time Interval', type: 'number', value: 0, min: 0 },
		{ label: 'Limit Value', type: 'number', value: 200, min: 0 },
	]);
	const location = useLocation();
	let flights = location.state.data;

	if (redirect.to.length > 0) {
		return <Navigate to={redirect.to} state={redirect.state} replace={redirect.replace} />;
	}

	function fetchOfferUnderLimit(key) {
		fetch('/api/get_offer_below_limit', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
				...convertFormDataToJSON(limitParams),
				flight_id: flights.offer_info[key].id,
				tracker_info: flights.tracker_info,
			}),
		})
			.then((res) => res.json())
			.then((data) => {
				setRedirect((prevRedirect) => ({
					...prevRedirect,
					to: '/payment-portal',
					state: { data: data.flight },
				}));
			});
	}

	function renderCards() {
		let allCards = [];
		for (let key in flights.offer_info) {
			let flight = flights.offer_info[key];
			let stops = flight.stops.replaceAll('\n', '<br />');

			allCards.push(
				<button key={key} className="flight-card" onClick={() => fetchOfferUnderLimit(key)}>
					<p dangerouslySetInnerHTML={{ __html: stops }}></p>
					<p>
						Price: {flight.total_amount} {flight.total_currency}
					</p>
				</button>
			);
		}
		return <div id="all_cards">{allCards}</div>;
	}

	return (
		<div>
			<img
				src={airplane}
				className="logo airplane"
				alt="Flight Limits"
				onClick={() => setRedirect((prevRedirect) => ({ ...prevRedirect, to: '/' }))}
			/>
			<h1>Flight Cards</h1>
			{Form(limitParams, setLimitParams)}
			{renderCards()}
		</div>
	);
}

export default FlightCard;
