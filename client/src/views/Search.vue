<template>
  <div id="search">
    <div class="tableWrapper">
      <div class="innerWrapper">
        <div class="table-actions">
          <input type="search" v-model="search" placeholder="Filter... " class="searchField" />
          <input type="button" value="+" @click.prevent="showModal = true" />
        </div>
        <table>
          <thead>
            <tr>
              <th>First Name</th>
              <th>Last Name</th>
              <th>Hours worked</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr :id="per.id" v-for="(per, index) in filterSearch" :key="index">
              <td>{{ per.first_name }}</td>
              <td>{{ per.last_name }}</td>
              <td class="numberTd">{{ per.hours_worked }}</td>
              <td>
                <input
                  class="deleteButton"
                  type="submit"
                  @click.prevent="delPerson(per.id, index)"
                  value="Delete"
                />
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <formModal v-if="showModal" @close="showModal = false" />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

import formModal from '../components/Form/formModal.vue';

@Component({ components: { formModal } })

export default class Search extends Vue {
  private showModal = false;
  private search = '';
  get filterSearch() {
    return this.$store.getters.getPersons.filter((data: any) => {
      return (
        `${data.first_name.toLowerCase()} ${data.last_name.toLowerCase()}`.includes(
          this.search.toLowerCase(),
        ) || data.hours_worked.includes(this.search)
      );
    });
  }
  private async created() {
    await this.$store.dispatch('LOAD_PERSONS');
  }
  private async delPerson(id: number, index: number) {
    await this.$store.dispatch('DELETE_PERSON', { id, index });
  }
}
</script>
<style scoped>
.table-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.searchField {
  background: transparent;
  max-width: 170px;
  font-size: 15px;
  border: none;
  outline: none;
  font-weight: bold;
  color: #2c3e50;
  height: 20px;
  border-bottom: 1px solid #2c3e50;
}

.searchField::placeholder {
  opacity: 0.5;
  color: #2c3e50;
}

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
  margin-right: 10px;
  width: auto;
  border: 1px solid #2c3e50;
  transition: ease-in-out 0.1s;
}

.tableWrapper input[type="button"]:hover {
  opacity: 1;
  color: #b4c2ce;
  background: #2c3e50;
}

.tableWrapper input[type="button"]:active {
  opacity: 0.8;
  color: #b4c2ce;
  background: #2c3e50;
}

.innerWrapper {
  display: block;
  margin: 0 auto;
}

td,
th {
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
  transition: ease-in-out 0.2s;
}

.deleteButton:hover {
  opacity: 1;
  color: #b4c2ce;
  background: #2c3e50;
}

.deleteButton:active {
  opacity: 0.8;
  color: #b4c2ce;
  background: #2c3e50;
}
</style>
