import { copyArray } from './HelperFunctions';

export function Form(inputs, setInputsFunc) {
	let form = [];
	for (let i = 0; i < inputs.length; i++) {
		let input = inputs[i];
		form.push(
			<div key={i}>
				<label>
					{input.label}:{' '}
					<input
						type={input.type}
						value={input.value}
						onChange={(e) => {
							let new_arr = copyArray(inputs);
							new_arr[i].value = e.target.value;
							setInputsFunc(new_arr);
						}}
						min={input.min}
						max={input.max}
					/>
				</label>
				<br />
			</div>
		);
	}
	return <form>{form}</form>;
}

export function convertFormDataToJSON(formData) {
	let rtnJSON = { indices: {}, data: formData };
	for (let i = 0; i < formData.length; i++) {
		rtnJSON.indices[formData[i].label] = i;
	}
	return rtnJSON;
}

export function MultiForm(inputs, setInputsFunc) {
	let multi_form = [];
	for (let i = 0; i < inputs.length; i++) {
		let form = [];
		for (let j = 0; j < inputs[i].length; j++) {
			let input = inputs[i][j];
			form.push(
				<div key={j}>
					<label>
						{input.label}:{' '}
						<input
							type={input.type}
							value={input.value}
							onChange={(e) => {
								let multi_form_copy = copyArray(inputs);
								multi_form_copy[i][j].value = e.target.value;
								setInputsFunc(multi_form_copy);
							}}
							min={input.min}
							max={input.max}
						/>
					</label>
					<br />
				</div>
			);
		}
		multi_form.push(
			<div key={i}>
				<form>{form}</form>
				<br />
			</div>
		);
	}

	return <div>{multi_form}</div>;
}
