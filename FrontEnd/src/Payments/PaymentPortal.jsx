import { useState, useEffect } from 'react';
import { Navigate, useLocation } from 'react-router-dom';
import { MainImage, MultiForm, copyArray, fetch_post } from '../Globals/Globals';

function PaymentPortal(props) {
	const [redirect, setRedirect] = useState({ to: '', state: {}, replace: false });
	const template_passenger_form = [
		{ label: 'First Name', type: 'text', value: 'Stephen' },
		{ label: 'Last Name', type: 'text', value: 'Giang' },
		{ label: 'Title', type: 'text', value: 'Mr' },
		{ label: 'Date of Birth', type: 'date', value: '2000-03-02' },
		{ label: 'Gender', type: 'text', value: 'M' },
		{ label: 'Phone Number', type: 'tel', value: '+18582165827' },
		{ label: 'Email', type: 'email', value: 'StephenG753@Gmail.com' },
	];
	const [passengersParams, setPassengersParams] = useState([]);
	const location = useLocation();
	let flight = location.state.data;
	const numAdults = Object.keys(flight.adults).length;
	const numChildren = Object.keys(flight.children).length;
	const numInfants = Object.keys(flight.infants).length;

	useEffect(() => {
		let all_passenger_forms = [];
		let type_passengers = [
			{ type: 'Adult', count: numAdults },
			{ type: 'Child', count: numChildren },
			{ type: 'Infant', count: numInfants },
		];
		for (let i = 0; i < type_passengers.length; i++) {
			let form_params = copyArray(template_passenger_form);
			for (let j = 0; j < form_params.length; j++) {
				form_params[j].label = type_passengers[i].type + ' ' + form_params[j].label;
			}
			all_passenger_forms = all_passenger_forms.concat(Array(type_passengers[i].count).fill(form_params));
		}
		setPassengersParams(all_passenger_forms);
	}, []);

	if (redirect.to.length > 0) {
		return <Navigate to={redirect.to} state={redirect.state} replace={redirect.replace} />;
	}

	function convertMultiFormDataToJSON() {
		let rtnJSON = { adults: {}, children: {}, infants: {} };
		let key = '';
		let idx = 0;
		for (let i = 0; i < passengersParams.length; i++) {
			if (i < numAdults) {
				key = 'adults';
				idx = i;
			} else if (i >= numAdults && i < numAdults + numChildren) {
				key = 'children';
				idx = i - numAdults;
			} else {
				key = 'infants';
				idx = i - (numAdults + numChildren);
			}
			rtnJSON[key][idx] = { indices: {}, data: passengersParams[i] };
			for (let j = 0; j < passengersParams[i].length; j++) {
				rtnJSON[key][idx].indices[passengersParams[i][j].label] = j;
			}
		}
		return rtnJSON;
	}

	function fetchOrderFlight() {
		let api_link = '/api/order_flight';
		let body = JSON.stringify({ ...convertMultiFormDataToJSON(), flight_id: flight.id });
		let afterFunc = (data) => {
			setRedirect((prevRedirect) => ({ ...prevRedirect, to: '/success', state: { data: data.order } }));
		};

		fetch_post(api_link, body, afterFunc);
	}

	return (
		<div>
			<MainImage redirectFunc={setRedirect} />
			<h1>Payment Portal</h1>
			<br />
			{MultiForm(passengersParams, setPassengersParams)}
			<br />
			<button onClick={() => fetchOrderFlight()}>
				<h3>Place Order</h3>
			</button>
		</div>
	);
}

export default PaymentPortal;
