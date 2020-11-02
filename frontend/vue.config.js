const path = require("path");
const BundleTracker = require("webpack-bundle-tracker");

// Config
function initConfig() {
  const frontendDir = __dirname;
  const staticDir = path.join(frontendDir, "static");
  const templatesDir = path.join(frontendDir, "templates");
  return {
    staticDir: staticDir,
    templatesDir: templatesDir,
    jsDir: path.join(frontendDir, "src"),
    distDir: path.join(staticDir, "dist"),
    sassDir: path.join(frontendDir, "sass"),
    webpackStatsDir: path.join("static", "dist"),
    globalStyles: []
  };
}

const settings = initConfig();

module.exports = {
  runtimeCompiler: true,
  publicPath: "http://127.0.0.1:8080/dist",
  outputDir: settings.distDir,

  chainWebpack: config => {
    config
      .plugin("BundleTracker")
      .use(BundleTracker, [
        { path: settings.webpackStatsDir, filename: "webpack-stats.json" }
      ]);

    config.output.filename("bundle.js");

    config.optimization.splitChunks(false);

    config.resolve.alias.set("__STATIC__", "static");

    config.devServer
      // the first 3 lines of the following code have been added to the configuration
      .public("http://127.0.0.1:8080")
      .host("127.0.0.1")
      .port(8080)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .disableHostCheck(true)
      .headers({ "Access-Control-Allow-Origin": ["*"] });
  }

  // uncomment before executing 'npm run build'
  // css: {
  //     extract: {
  //       filename: 'bundle.css',
  //       chunkFilename: 'bundle.css',
  //     },
  // }
};
