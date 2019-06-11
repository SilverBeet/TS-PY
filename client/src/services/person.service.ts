import Axios from 'axios';

const url = 'http://127.0.0.1:5000/person';

export default {
  async getAllPosts() {
    return await Axios.get(`${url}`);
  },

  submitPerson(data: object) {
    Axios.post(`${url}`, data);
  },

  deletePerson(id: string) {
    Axios.delete(`${url}/${id}`);
  },
};
