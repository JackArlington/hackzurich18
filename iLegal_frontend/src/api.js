import axios from 'axios';
const API_ROOT = `https://159.69.197.71:5000/`;

const requests = {
	delete: url => axios.delete(`${API_ROOT}${url}`),
	get: (url, params) => axios.get(`${API_ROOT}${url}`, params),
	patch: (url, body) => axios.patch(`${API_ROOT}${url}`, body),
	post: (url, body) => axios.post(`${API_ROOT}${url}`, body),
	put: (url, body) => axios.put(`${API_ROOT}${url}`, body),
};

export const API = {
	getCatchphrase: (STTResponse) => requests.post(`ai`, STTResponse)
}
