export default class Http {

    static baseUrl = 'http://127.0.0.1:8000'

    static addParamsToGet(url, params = {}) {
        const urlWithParams = new URL(Http.baseUrl + url);
        Object.keys(params).forEach(key => urlWithParams.searchParams.append(key, params[key]));
        return urlWithParams;
    }

    static get(url, params = {}) {
        const urlWithParams = Http.addParamsToGet(url, params)
        return fetch(urlWithParams, {
            headers: {
                'Accept': 'application/json'
            }
        });
    }

    static post(url, params = {}) {
        return fetch(Http.baseUrl + url, {
            body: JSON.stringify(params),
            method: 'post',
            headers: {
                'Accept': 'application/json'
            }
        });
    }
}