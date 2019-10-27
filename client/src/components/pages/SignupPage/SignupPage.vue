<template>
  <div>
    <h1>Signup</h1>
    <b-form @submit="onSubmit" id="signup-form">

      <!--Email input-->
      <b-form-group
        :invalid-feedback="invalidEmail"
        :state="emailState"
        label="Email"
        label-for="email-input"
      >
        <b-form-input :state="emailState" id="email-input" required type="email"
                      v-model="form.email">
        </b-form-input>
      </b-form-group>

      <!--Password input-->
      <b-form-group
        label="Password"
        label-for="password-input"
        :state="passwordState"
        :invalid-feedback="invalidPassword"
      >
        <b-form-input id="password-input" required type="password" :state="passwordState"
                      v-model="form.password"></b-form-input>
      </b-form-group>

      <!--Password confirm input-->
      <b-form-group
        :invalid-feedback="invalidConfirmPassword"
        :state="confirmPasswordState"
        label="Confirm Password"
        label-for="confirm-password-input"
      >
        <b-form-input :state="confirmPasswordState" id="confirm-password-input" required
                      type="password" v-model="form.confirmPassword"
        ></b-form-input>
      </b-form-group>

      <!--Personal database ID input-->
      <b-form-group
        description="If you exist in the database, please enter your ID. The ID is the last part of the url (after the /id/) of a personal file, like this: hegardt/person/id/000000000000000000100182"
        label="Personal Database ID"
        label-for="person-id-input"
      >
        <b-form-input id="person-id-input" v-model="form.personId"></b-form-input>
      </b-form-group>

      <!--Confirm Button-->
      <b-button type="submit" variant="primary">Sign up</b-button>
    </b-form>
  </div>
</template>

<script>
  export default {
    name: "SignupPage",
    data() {
      return {
        form: {
          email: "",
          password: "",
          confirmPassword: "",
          personId: ""
        },
        email_regexp: new RegExp(`(.+)@(.+)\\.(.+)`)
      }
    },
    computed: {
      invalidEmail() {
        return "Please enter a valid email address.";
      },
      emailState() {
        let e = this.form.email;
        if (e.length === 0)
          return null;
        return !!(e && e.match(this.email_regexp));
      },
      invalidPassword(){
        return "Password must be longer than 6 symbols!";
      },
      passwordState() {
        let p = this.form.password;
        if (p.length === 0)
          return null;
        return !!(p.length >= 6);
      },
      invalidConfirmPassword() {
        return "Passwords do not match!";
      },
      confirmPasswordState() {
        let p = this.form.password;
        let cp = this.form.confirmPassword;
        if (!this.passwordState || cp.length === 0)
          return null;
        return !!(p === cp);
      }
    },
    methods: {
      onSubmit() {
        console.log("Signing up!");
      },

    }
  }
</script>

<style scoped>
  #signup-form {
    margin: auto;
    width: 50%;
  }
</style>
