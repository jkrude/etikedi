import * as getters from "./getters";
import * as actions from "./actions";
import * as mutations from "./mutations";
import {State} from "./models";

const debug = process.env.NODE_ENV !== "production";

const state: State = {
    loading: false,
    prevButtonDisabled: false,
    nextButtonDisabled: false,
    displayFeatureTooltips: true,
    allDatasets: [],
    currentDataset: "",
    cifarSampleID: "",
    cifarSample: undefined,
    cifarLabels: []
};

export const cifarStore = {
    state,
    getters,
    actions,
    mutations,
    modules: {},
    strict: debug,
    namespaced: true // Important! else these will conflict with the root store! see https://vuex.vuejs.org/guide/modules.html
};
