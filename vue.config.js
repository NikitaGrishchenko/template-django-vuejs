const path = require('path')
const BundleTracker = require('webpack-bundle-tracker')
const isProd = process.env.NODE_ENV === 'production'

// Config
function initConfig() {
  const frontendDir = path.join(__dirname, 'frontend')
  const staticDir = path.join(frontendDir, 'static')
  const templatesDir = path.join(frontendDir, 'templates')
  return {
    staticDir: staticDir,
    templatesDir: templatesDir,
    jsDir: path.join(frontendDir, 'js'),
    distDir: path.join(staticDir, 'dist'),
    sassDir: path.join(frontendDir, 'sass'),
    webpackStatsDir: path.join('frontend', 'static', 'dist'),
    globalStyles: []
  }
}

const settings = initConfig()

module.exports = {
  runtimeCompiler: true,
  publicPath: isProd ? '/static/dist' : 'http://localhost:8080/dist',
  outputDir: settings.distDir,

  chainWebpack: config => {
    config
      .entry('app')
      .clear()
      .add('./frontend/js/main.js')
      .end()
    config
      .plugin('BundleTracker')
      .use(BundleTracker, [
        { path: settings.webpackStatsDir, filename: 'webpack-stats.json' }
      ])

    config.output.filename('bundle.js')

    config.optimization.splitChunks(false)

    config.resolve.alias.set('__STATIC__', 'static')

    config.devServer
      // the first 3 lines of the following code have been added to the configuration
      .public('http://127.0.0.1:8080')
      .host('localhost')
      .port(8080)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .contentBase(settings.templatesDir)
      .watchContentBase(true)
      .disableHostCheck(true)
      .headers({ 'Access-Control-Allow-Origin': ['*'] })
  }

  // uncomment before executing 'npm run build'
  // css: {
  //     extract: {
  //       filename: 'bundle.css',
  //       chunkFilename: 'bundle.css',
  //     },
  // }
}
