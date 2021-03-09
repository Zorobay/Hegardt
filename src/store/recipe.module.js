import {FETCH_ALL_RECIPES, FETCH_RECIPE_BY_TITLE} from './actions.type';
import {ADD_RECIPE_TO_HASH, SET_ALL_RECIPES} from './mutations.type';
import {RecipeService} from '@/common/api.service';


export const state = {
  allRecipesFetched: false,
  recipes: [],
  recipesHash: new Map(),
};

export const mutations = {
  [SET_ALL_RECIPES](state, allRecipes) {
    state.recipes = allRecipes;
    state.allRecipesFetched = true;

    for (const r of allRecipes) {
      state.recipesHash.set(r.title, r);
    }
  },
  [ADD_RECIPE_TO_HASH](state, recipe) {
    state.recipesHash.set(recipe.title, recipe);
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
    // First, check if the recipe is in the hash map
    if (state.recipesHash.has(title)) {
      return new Promise((resolve, reject) => {
        resolve(state.recipesHash.get(title));
      });
    } else {
      return RecipeService.getRecipeByTitle(title)
          .then(recipes => {
            if (recipes.length === 1) {
              context.commit(ADD_RECIPE_TO_HASH, recipes[0]);
              return recipes[0];
            } else {
              if (recipes.length > 1) {
                reject(`Recipe title ${title} does not appear to be unique, and returned more than one recipe!`);
              } else {
                reject(`No recipe with title ${title} found!`);
              }
            }
          });
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
