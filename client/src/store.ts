import Vue from 'vue';
import Vuex from 'vuex';

import PersonService from './services/person.service';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    persons: [] as object[],
  },
  getters: {
    getPersons: (state) => state.persons,
  },
  mutations: {
    setPersons: (state, persons: object[]) => {
      state.persons = persons;
    },
    removePerson: (state, index: number) => {
      state.persons.splice(index, 1);
    },
    updatePersons: (state, form: object) => {
      state.persons.push(form);
    },
  },
  actions: {
    CREATE_PERSON: async ({ commit }, form: object) => {
      await PersonService.create(form);
      commit('updatePersons', form);
    },
    LOAD_PERSONS: async ({ commit }) => {
      try {
        const persons = await PersonService.getAll();
        commit('setPersons', persons.data);
      } catch (error) {
        console.log(error);
      }
    },
    DELETE_PERSON: async ({ commit }, { id, index }) => {
      await PersonService.deletePerson(id);
      commit('removePerson', index);
    },
  },
});

export default store;
