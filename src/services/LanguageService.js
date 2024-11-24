import language from "../db/language.js";

export default class LanguageService {

    constructor() {
        this._lang = language;
    }

    resolveKey(key) {
        const lang = this._lang[Hegardt.language];
        const keys = key.split('.');
        let subLang = lang;
        keys.forEach(k => {
            subLang = subLang[k];
        })
        return subLang;
    }
}
