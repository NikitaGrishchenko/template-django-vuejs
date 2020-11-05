import Vue from "vue";
import App from "./App";
[App].forEach(Component => {
  if (!Component.name) {
    throw new Error(`Not component name: ${Component}`);
  }

  Vue.component(Component.name, Component);
});
