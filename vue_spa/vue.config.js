const BundleTracker = require("webpack-bundle-tracker");
const target = "http://127.0.0.1:8000";

module.exports = {
  publicPath: "http://127.0.0.1:8080/",
  outputDir: "./dist/",

  chainWebpack: (config) => {
    config.optimization.splitChunks(false);
    config
      .plugin("BundleTracker")
      .use(BundleTracker, [{ filename: "./webpack-stats.json" }]);
    config.devServer
      .public("http://0.0.0.0:8080")
      .host("0.0.0.0")
      .port(8080)
      .https(false)
      .headers({ "Access-Control-Allow-Origin": ["*"] });
    config.plugins.delete("prefetch");
  },

  pages: {
    index: "src/main.js"
  },

  devServer: {
    port: 8080,
    proxy: {
      "/list": {
        target,
        chagneOrigin: true
      }
    }
  }
};
