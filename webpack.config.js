const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const fs = require('fs');
const CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports = {
  entry: './Working_Directory/game.html', // The HTML file as the entry point
  output: {
    path: path.resolve(__dirname, 'Output'), // Output to 'Output' directory
    filename: 'bundle.js', // Output bundle file
  },
  module: {
    rules: [
      {
        test: /\.html$/,
        use: ['html-loader'], // Handle HTML files
      },
      {
        test: /\.(mp3)$/,
        type: 'asset/inline', // Inline MP3 files as base64
        generator: {
          dataUrl: (content) => `data:audio/mp3;base64,${content.toString('base64')}`,
        },
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      filename: 'game.html', // Output HTML file with a different name
      template: './Working_Directory/game.html', // Use the template HTML file
    }),
    new CopyWebpackPlugin({
      patterns: [
        {
          from: path.resolve(__dirname, 'Working_Directory'),
          to: path.resolve(__dirname, 'Output'),
          globOptions: {
            // Only copy specific files (e.g., images, other assets) and exclude MP3 files
            ignore: ['**/*.mp3'], // Exclude MP3 files
          },
          // Copy only specific file types (e.g., images, other assets)
          noErrorOnMissing: true,
          filter: (resourcePath) => {
            // Specify which files to include; exclude HTML and JS files as they are handled by other loaders
            return /\.(png|jpg|jpeg|gif|svg|json)$/.test(resourcePath);
          },
        },
      ],
    }),
  ],
  mode: 'development', // Set mode to 'development' or 'production'
};
