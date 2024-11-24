$(document).ready(() => {

    const languageMenu = $('#navbar-language-menu');

    const setActiveLanguage = function () {
        const languageMenuItem = languageMenu.find(`li[value="${Hegardt.language}"] a`);
        languageMenuItem.addClass('active');
    }

    setActiveLanguage();
})
