const VueLoaderPlugin = require('vue-loader/lib/plugin');


module.exports = {
  entry: './src/main.js',
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader',
      },
      // this will apply to both plain `.js` files
      // AND `<script>` blocks in `.vue` files
      {
        test: /\.js$/,
        loader: 'babel-loader',
      },
      // this will apply to both plain `.css` files
      // AND `<style>` blocks in `.vue` files
      {
        test: /\.css$/i,
        use: [
          'vue-style-loader',
          'css-loader',
        ],
      },
      {
        test: /.(png|svg|jpg|jpeg|gif|json)$/i,
        loader: 'file-loader',
      },
      {
        test: /\.scss$/,
        loader: 'sass-loader',
      },
    ],
  },
  plugins: [
    new VueLoaderPlugin(),
  ],
};
