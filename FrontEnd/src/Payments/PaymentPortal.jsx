import { useState, useEffect } from 'react';
import { Navigate, useLocation } from 'react-router-dom';
import { MultiForm } from '../Globals/Form';
import { copyArray } from '../Globals/ArrayCopy';
import '../css/master.css';
import airplane from '../assets/airplane.gif';

function PaymentPortal() {
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
	const numAdults = Object.keys(flight.passengers).length;
	const numInfants = Object.keys(flight.infants).length;

	useEffect(() => {
		let adult_form_params = copyArray(template_passenger_form);
		let infant_form_params = copyArray(template_passenger_form);
		for (let i = 0; i < adult_form_params.length; i++) {
			adult_form_params[i].label = 'Adult ' + adult_form_params[i].label;
		}
		for (let i = 0; i < infant_form_params.length; i++) {
			infant_form_params[i].label = 'Infant ' + infant_form_params[i].label;
		}
		let all_passenger_form_params = [];
		for (let i = 0; i < numAdults; i++) {
			all_passenger_form_params.push(adult_form_params);
		}
		for (let i = 0; i < numInfants; i++) {
			all_passenger_form_params.push(infant_form_params);
		}
		setPassengersParams(all_passenger_form_params);
	}, []);

	if (redirect.to.length > 0) {
		return <Navigate to={redirect.to} state={redirect.state} replace={redirect.replace} />;
	}

	function convertMultiFormDataToJSON() {
		let rtnJSON = { adults: {}, infants: {} };
		let i = 0;
		while (i < numAdults) {
			rtnJSON.adults[i] = { indices: {}, data: passengersParams[i] };
			for (let j = 0; j < passengersParams[i].length; j++) {
				rtnJSON.adults[i].indices[passengersParams[i][j].label] = j;
			}
			i++;
		}
		while (i < passengersParams.length) {
			rtnJSON.infants[i - numAdults] = { indices: {}, data: passengersParams[i] };
			for (let j = 0; j < passengersParams[i].length; j++) {
				rtnJSON.infants[i - numAdults].indices[passengersParams[i][j].label] = j;
			}
			i++;
		}
		return rtnJSON;
	}

	function fetchOrderFlight() {
		fetch('/api/order_flight', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({ ...convertMultiFormDataToJSON(), flight_id: flight.id }),
		})
			.then((res) => res.json())
			.then((data) => {
				console.log(data.order.id);
			});
	}

	return (
		<div>
			<img
				src={airplane}
				className="logo airplane"
				alt="Flight Limits"
				onClick={() => setRedirect((prevRedirect) => ({ ...prevRedirect, to: '/' }))}
			/>
			<h1 onClick={() => createAllPassengerFormData()}>Payment Portal</h1>
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
