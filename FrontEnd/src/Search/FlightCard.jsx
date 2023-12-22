import { useState } from 'react';
import { useLocation, Navigate } from 'react-router-dom';
import '../css/master.css';
import airplane from '../assets/airplane.gif';

function FlightCard(props) {
	const [redirect, setRedirect] = useState({ to: '', state: {}, replace: false });
	const [limitParams, setLimitParams] = useState({ maxIterations: 25, timeInterval: 0, limitVal: 200 });
	const [plotPath, setPlotPath] = useState('');
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
				id: flights.offer_info[key].id,
				maxIterations: Number(limitParams.maxIterations),
				timeInterval: Number(limitParams.timeInterval),
				limitVal: Number(limitParams.limitVal),
				trackerInfo: flights.tracker_info,
			}),
		})
			.then((res) => res.json())
			.then((data) => {
				setPlotPath('src/assets_test/' + data.plot);
				setRedirect((prevRedirect) => ({
					...prevRedirect,
					to: '/payment-portal',
					state: { flight: data.flight },
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

	function form() {
		return (
			<form>
				<label>
					Max Iterations:{' '}
					<input
						type="number"
						value={limitParams.maxIterations}
						onChange={(e) => setLimitParams({ ...limitParams, maxIterations: e.target.value })}
						min={0}
					/>
				</label>
				<br />
				<label>
					Time Interval:{' '}
					<input
						type="number"
						value={limitParams.timeInterval}
						onChange={(e) => setLimitParams({ ...limitParams, timeInterval: e.target.value })}
						min={0}
					/>
				</label>
				<br />
				<label>
					Limit Value:{' '}
					<input
						type="number"
						value={limitParams.limitVal}
						onChange={(e) => setLimitParams({ ...limitParams, limitVal: e.target.value })}
						min={0}
					/>
				</label>
				<br />
			</form>
		);
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
			{form()}
			{renderCards()}
			<img src={plotPath} className="logo airplane" />
		</div>
	);
}

export default FlightCard;
