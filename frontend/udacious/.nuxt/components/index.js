export { default as Header } from '../..\\components\\Header.vue'
export { default as Logo } from '../..\\components\\Logo.vue'
export { default as Project } from '../..\\components\\Project.vue'

export const LazyHeader = import('../..\\components\\Header.vue' /* webpackChunkName: "components_Header'}" */).then(c => c.default || c)
export const LazyLogo = import('../..\\components\\Logo.vue' /* webpackChunkName: "components_Logo'}" */).then(c => c.default || c)
export const LazyProject = import('../..\\components\\Project.vue' /* webpackChunkName: "components_Project'}" */).then(c => c.default || c)
