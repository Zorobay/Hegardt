<template>
  <div>
    <h1>Login</h1>
    <b-alert v-model="missingUserAlert" variant="danger">User with email <b>{{form.email}}</b> does
      not
      exist!
      <router-link :to="{name: 'SignupPage'}">Click here</router-link> to sign up.</b-alert>
    <b-form @submit="onSubmit" id="login-form">
      <b-form-group
        label="Email"
        label-for="email-input"
      >
        <b-form-input id="email-input" v-model="form.email"></b-form-input>
      </b-form-group>
      <b-form-group
        label="Password"
        label-for="password-input"
        :invalid-feedback="passwordInvalid"
        :state="passwordState"
      >
        <b-form-input id="password-input" type="password" v-model="form.password"
                      :state="passwordState"></b-form-input>
      </b-form-group>

      <b-button type="submit" variant="primary">Login</b-button>
    </b-form>
  </div>
</template>

<script>

  import {UserService} from "../../../common/api.service";

  export default {
    name: "LoginPage",
    data() {
      return {
        missingUserAlert: false,
        wrongPass: false,
        form: {
          email: "",
          password: ""
        }
      }
    },
    computed: {
      passwordInvalid(){
        return "Invalid Password!";
      },
      passwordState() {
        if (this.wrongPass)
          return false;
        return null;
      }
    },
    methods: {
      onSubmit() {
        UserService.authenticateUser(this.form)
          .then(res => {
            if (res.status === 200) { // Login succeeded!
              this.$router.push({name: 'HegardtPage'});
            }
          })
          .catch(err => {
            const res = err.response;
            if (res.status === 401) { // Authentication error!
              if (res.data.code === "USER_WRONG_PASSWORD") {
                this.wrongPass = true;
              } else if (res.data.code === "USER_MISSING") {
                this.missingUserAlert = true;
              }
            }
          });
      }
    }
  }
</script>

<style scoped>
  #login-form {
    margin: auto;
    width: 40%;
  }
</style>
