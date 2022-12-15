<template>
  <div class="row">
    <div class="col-md-2">
      <nav id="toc"></nav>
    </div>
    <div class="col-md-10">
      <h1>
        Recept
        <b-spinner v-if="!loaded"></b-spinner>
      </h1>
      <div v-for="cat in categories" :key="cat">
        <h2>{{cat}}</h2>
        <h6 v-for="recipe in recipesPerCategory[cat]" :key="recipe.title">
          <router-link :to="{name: 'RecipePage', params: {title: recipe.title}}">
            {{recipe.title}}
          </router-link>
        </h6>
      </div>
    </div>
  </div>
</template>

<script>
  import {FETCH_ALL_RECIPES} from '../../../store/actions.type';
  const $ = require('jquery');

  export default {
    name: 'RecipesPage',

    data: () => ({
      loaded: false,
    }),
    computed: {
      lang() {
        return this.$store.getters.language;
      },
      recipes() {
        return this.$store.getters.recipes;
      },
      categories() {
        const cats = new Set();
        for (const r of this.recipes) {
          cats.add(r.category);
        }
        return cats;
      },
      recipesPerCategory() {
        const rpc = {};
        for (const r of this.recipes) {
          let cat = r.category;
          if (!cat) {
            cat = 'No Category';
          }

          if (rpc.hasOwnProperty(cat)) {
            rpc[cat].push(r);
          } else {
            rpc[cat] = [r];
          }
        }
        return rpc;
      },
    },
    created() {
      if (!this.$store.getters.allRecipesFetched) {
        this.$store.dispatch(FETCH_ALL_RECIPES)
          .then(res => {
            this.loaded = true;
            this.initToc();
          });
      } else {
        this.loaded = true;
      }
    },
    methods: {
      initToc() {
        $(function() {
          const navSelector = '#toc';
          const $myNav = $(navSelector);
          Toc.init($myNav);
          $('body').scrollspy({
            target: navSelector,
          });
        });
      },
    },
  };
</script>

<style scoped>

</style>
