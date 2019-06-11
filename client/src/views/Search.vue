<template>
  <div id="search">
    <div class="tableWrapper">
      <div class="innerWrapper">
        <input type="button" value="Add" @click.prevent="showModal = true">
        <table>
          <thead>
            <tr>
              <th>First name</th>
              <th>Last name</th>
              <th>Hours worked</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr :id="item.id" v-for="(item, index) in person" :key="index">
              <td>{{ item.first_name }}</td>
              <td>{{ item.last_name }}</td>
              <td class="numberTd">{{ item.hoursWorked }}</td>
              <td><input class="deleteButton" type="submit" @click.prevent="delPerson(item.id, index)" value="Delete"></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <formModal v-if="showModal" @close="showModal = false" />
  </div>
</template>

<script lang="ts">

// Dependencies
import { Component, Vue, Prop } from 'vue-property-decorator';
import Axios from 'axios';

// Api Service
import Persons from '../services/person.service';

// Components
import formModal from '../components/Form/formModal.vue';
interface IPerson {
  first_name: string;
  last_name: string;
  hoursWorked: number;
}

@Component({components: { formModal } })

export default class Search extends Vue {

  public person: IPerson[] = [];

  private showModal = false;

  private showAllPosts() {
    Persons.getAllPosts()
      .then((res) => this.person = res.data)
      .catch((err) => console.log(err));
  }

  private created() {
    this.showAllPosts();
  }

  private delPerson(id: string, index: number) {
    Persons.deletePerson(id);
    this.person.splice(index, 1);

  }

}
</script>

<style scoped>

table {
  border-collapse: collapse;
  margin-bottom: 50px;
}

.tableWrapper {
  display: flex;
}

.tableWrapper input[type="button"] {
  color: #2c3e50;
  background: transparent;
  cursor: pointer;
  outline: none;
  font-weight: bold;
  font-size: 15px;
  width: auto;  
  border: 1px solid #2c3e50;
  transition: ease-in-out .1s;
  margin-bottom: 20px;
}

.tableWrapper input[type="button"]:hover {
  opacity: 1;
  color: #b4c2ce;
  background: #2c3e50;
}

.tableWrapper input[type="button"]:active {
  opacity: .8;
  color: #b4c2ce;
  background: #2c3e50;
}

.innerWrapper {
  display: block;
  margin: 0 auto;
}

td, th {
  padding: 10px;
  text-align: left;
  border: none;
  border-bottom: 1px solid #2c3e50;
}

.numberTd {
  text-align: right;
}

.deleteButton {
  color: #2c3e50;
  background: transparent;
  cursor: pointer;
  outline: none;
  font-weight: bold;
  font-size: 15px;
  border: 1px solid #2c3e50;
  transition: ease-in-out .2s;
}

.deleteButton:hover {
  opacity: 1;
  color: #b4c2ce;
  background: #2c3e50;
}

.deleteButton:active {
  opacity: .8;
  color: #b4c2ce;
  background: #2c3e50;
}

</style>
