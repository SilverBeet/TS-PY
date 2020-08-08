<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="close" @click="$emit('close')"  >x</div>
            <div id="inputform">
            <form>
              <div class="inputWrapper">
                <label for="firstName">First Name</label>
                <input id="firstName" v-model="form.first_name" name="first_name" required type="text">
              </div>
              <div class="inputWrapper">
                <label for="lastName">Last Name</label>
                <input id="lastName"  v-model="form.last_name" name="last_name" required type="text">
              </div>
              <div class="inputWrapper">
                <label for="hoursWorked">Hours worked</label>
                <input id="hoursWorked"  v-model="form.hoursWorked" name="hoursWorked" required type="number">
              </div>
              <div class="submitWrapper">
                <input type="submit" @click.prevent="createNew" value="Send">
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Persons from '../../services/person.service';

interface IForm {
  first_name: string;
  last_name: string;
  hoursWorked: number | '';
}

@Component
export default class Form extends Vue {
  private form: IForm = {
    first_name: '',
    last_name: '',
    hoursWorked: '',
  };
  private async createNew() {
    if (this.form.first_name === '' || this.form.last_name === '' || this.form.hoursWorked === '') { return; }
    await this.$store.dispatch('CREATE_PERSON', this.form);
    this.cleanForm();
  }
  private cleanForm() {
    this.form = {
      first_name: '',
      last_name: '',
      hoursWorked: '',
    };
  }
}
</script>

<style>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: table;
  background-color: rgba(0, 0, 0, .5);
  transition: opacity .3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 300px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
  transition: all .3s ease;
  font-family: Helvetica, Arial, sans-serif;
}



.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}

.close {
  float: right;
  color:#2c3e50;
  font-size: 20px;
  cursor: pointer;
}

#inputform  {
  display: grid;
  grid-template-columns: 200px; 
  justify-content: center;
}

.inputWrapper {
  margin: 30px auto;
  max-width: 170px;
}

.inputWrapper input[type="text"] {
  background: #fff;
  max-width: 170px;
  font-size: 15px;
  border: none;
  outline: none;
  font-weight: bold;
  color: #2c3e50;
  border-bottom: 1px solid #2c3e50;
}

#hoursWorked {
  outline: none;
  max-width: 170px;
  font-weight: bold;
  color: #2c3e50;
  font-size: 15px;
  border: none;
  border-bottom: 1px solid #2c3e50;
  background: #fff;
}

#hoursWorked::-webkit-outer-spin-button,
#hoursWorked::-webkit-inner-spin-button {
  -webkit-appearance: none;
}

.inputWrapper label {
  opacity: .8;
  font-weight: bold;
  color: #2c3e50;
  font-size: 13px;
}

.submitWrapper {
  display: block;
  margin: 0 auto;
  text-align: center;
}

.submitWrapper input[type="submit"] {
  color: #2c3e50;
  background: transparent;
  cursor: pointer;
  outline: none;
  font-weight: bold;
  font-size: 15px;
  width: 50%;  
  border: 1px solid #2c3e50;
  transition: ease-in-out .04s;
}

.submitWrapper input[type="submit"]:hover {
  opacity: 1;
  color: #b4c2ce;
  background: #2c3e50;
}

.submitWrapper input[type="submit"]:active {
  opacity: .8;
  color: #b4c2ce;
  background: #2c3e50;
}
</style>
