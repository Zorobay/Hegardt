<template>
    <div v-if="recipe">
      <h1>{{recipe.title}}</h1>
      <div class="row">
        <div class="col-md-5">
          <p>
            <font-awesome-icon icon="clock"/>
            {{formatRange(recipe.portions)}} {{recipe.portion_unit}}
          </p>
        </div>
        <div class="col-md-1"></div>
        <div class="col-md-4">
          <p>
            <font-awesome-icon icon="users"/>
            {{formatRange(recipe.total_time)}} {{recipe.time_unit}}
          </p>
        </div>
      </div>
      <h5>{{recipe.description}}</h5>
      <div class="row">
        <div class="col-md-4 ingredients">
          <div v-for="ingr in recipe.ingredients" :key="ingr.title">
            <p>{{ingr.title}}</p>
            <ul>
              <li v-for="i in ingr.ingredients" :key="i">{{i}}</li>
            </ul>
          </div>
        </div>
        <div class="col-md-8 instructions">
          <div v-for="instr in recipe.instructions">
            <p>{{instr.title}}</p>
            <ol>
              <li v-for="i in instr.instructions" :key="i">{{i}}</li>
            </ol>
          </div>
        </div>
      </div>

    </div>
</template>

<script>

  import {FETCH_RECIPE_BY_TITLE} from '../../../store/actions.type';

  export default {
    name: 'RecipePage',
    data() {
      return {
        recipe: {},
      };
    },
    created() {
      const title = this.$route.params.title;
      this.$store.dispatch(FETCH_RECIPE_BY_TITLE, title)
        .then(res => {
          this.recipe = res[0];
        })
        .catch(err => this.$router.replace({name: 'MissingPage'}));
    },
  };
</script>

<style scoped>
  .ingredients li, .instructions li {
    text-align: left;
  }

  .ingredients p, .instructions p {
    font-weight: bold;
  }
</style>
