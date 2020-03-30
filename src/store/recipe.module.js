import {FETCH_ALL_RECIPES, FETCH_RECIPE_BY_TITLE} from './actions.type';
import {SET_ALL_RECIPES} from './mutations.type';
import {RecipeService} from '../common/api.service';


export const state = {
  allRecipesFetched: false,
  recipes: [],
};

export const mutations = {
  [SET_ALL_RECIPES](state, allRecipes) {
    state.recipes = allRecipes;
    state.allRecipesFetched = true;
  },
};

export const actions = {
  async [FETCH_ALL_RECIPES](context) {
    return RecipeService.getAllRecipes()
        .then(data => {
          context.commit(SET_ALL_RECIPES, data);
          return data;
        });
  },

  async [FETCH_RECIPE_BY_TITLE](context, title) {
    if (state.allRecipesFetched) {
      const recipe = state.recipes.filter(r => r.title === title);
      return new Promise((resolve, reject) => {
        console.log(recipe);
        if (recipe.length > 0) {
          resolve(recipe);
        } else {
          reject(`No recipe found with tile ${title}`);
        }
      });
    } else {
      return RecipeService.getRecipeByTitle(title);
    }
  },
};

export const getters = {
  recipes(state) {
    return state.recipes;
  },
  allRecipesFetched(state) {
    return state.allRecipesFetched;
  },
};

export default {
  state,
  actions,
  mutations,
  getters,
};
