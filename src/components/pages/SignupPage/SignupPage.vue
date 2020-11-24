<template>
  <div>
    <div v-if="!success">
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
          :invalid-feedback="invalidPassword"
          :state="passwordState"
          label="Password"
          label-for="password-input"
        >
          <b-form-input :state="passwordState" id="password-input" required type="password"
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
          :invalid-feedback="invalidUserId"
          :state="userIdState"
          description="If you exist in the database, please enter your ID. The ID is the last part of the url (after the /id/) of a personal file,
           like this: hegardt/person/id/000000000000000000100182"
          label="Personal Database ID"
          label-for="person-id-input"
        >
          <b-form-input :state="userIdState" id="person-id-input" v-model="form.person_id"></b-form-input>
        </b-form-group>

        <!--Confirm Button-->
        <b-button type="submit" variant="primary">Sign up</b-button>
      </b-form>
    </div>
    <div v-if="success">
      <h1 style="color: green;">Success! You've signed up!</h1>
      <h6>However, you need to confirm your email before using
        the account. Check the email we sent you and follow the link.</h6>
    </div>
  </div>
</template>

<script>
  import {UserService} from '../../../common/api.service';

  const ObjectId = require('mongoose').Types.ObjectId;

  export default {
    name: 'SignupPage',
    data() {
      return {
        form: {
          email: '',
          password: '',
          confirmPassword: '',
          person_id: '',
        },
        email_regexp: new RegExp('(.+)@(.+)\\.(.+)'),
        success: false,
        failed_exists: false,
      };
    },
    computed: {
      invalidEmail() {
        if (this.failed_exists) {
          return 'A user with that email already exists!';
        } else {
          return 'Please enter a valid email address.';
        }
      },
      emailState() {
        if (this.failed_exists) {
          return false;
        }

        const e = this.form.email;
        if (e.length === 0) {
          return null;
        }
        return !!(e && e.match(this.email_regexp));
      },
      invalidPassword() {
        return 'Password must be longer than 8 symbols!';
      },
      passwordState() {
        const p = this.form.password;
        if (p.length === 0) {
          return null;
        }
        return (p.length >= 8);
      },
      invalidConfirmPassword() {
        return 'Passwords do not match!';
      },
      confirmPasswordState() {
        const p = this.form.password;
        const cp = this.form.confirmPassword;
        if (!this.passwordState || cp.length === 0) {
          return null;
        }
        return (p === cp);
      },
      userIdState() {
        const id = this.form.person_id;
        if (!id) {
          return null;
        }
        return !!(ObjectId.isValid(id) && new ObjectId(id).toString() === id);
      },
      invalidUserId() {
        return 'This is not a valid ID!';
      },
    },
    methods: {
      onSubmit() {
        const user = {
          email: this.form.email,
          password: this.form.password,
          person_id: this.form.person_id,
        };
        UserService.registerUser(user)
          .then(res => {
            if (res.status === 201) {
              this.success = true;
            }
          })
          .catch(err => {
            if (err.response.status === 422) {
              const data = err.response.data.errors;
              if (data.length > 1) {
                throw err;
              } else {
                const err0 = data[0];
                if (err0.param === 'email') {
                  this.failed_exists = true;
                }
              }
            } else {
              throw err;
            }
          });
      },

    },
  };
</script>

<style scoped>
  #signup-form {
    margin: auto;
    width: 40%;
  }
</style>
