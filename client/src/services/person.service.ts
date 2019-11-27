import Axios from 'axios';

const url = 'http://127.0.0.1:5000/person';

export default {
  async getAll() {
    return await Axios.get(`${url}`);
  },

  async create(data: object) {
    await Axios.post(`${url}`, data);
  },

  async deletePerson(id: string) {
    await Axios.delete(`${url}/${id}`);
  },
};
