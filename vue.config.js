module.exports =
{
  // This is all needed as otherwise linting will only be performed on changed files.
  // TODO Remove this in the future.
  chainWebpack: config => {
    config.module.rule('eslint').use('eslint-loader').loader('eslint-loader').tap(options => {
      delete options.cacheIdentifier;
      options.cache = false; // otherwise on each restart cached errors won't be shown !!!
      return options;
    });
    config.module.rule('vue').use('vue-loader').loader('vue-loader').tap(options => {
      delete options.cacheDirectory;
      return options;
    });
    config.module.rule('vue').uses.delete('cache-loader');
    config.module.rule('js').uses.delete('cache-loader');
  },
};
