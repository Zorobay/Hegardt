import api from './axios';
import type { AxiosResponse } from 'axios';
import type { EntityId, Person, PersonsMap, PersonSummary, PersonTreeRoot } from '@/types/person.type.ts';

export const personsApiService = {
  getSummaryById: (id: EntityId): Promise<AxiosResponse<PersonSummary>> => api.get(`/persons/getSummaryById/${id}`),

  getCompleteById: (id: EntityId): Promise<AxiosResponse<Person>> => api.get(`/persons/getCompleteById/${id}`),

  findByName: (name: string): Promise<AxiosResponse<Person[]>> => api.get(`/persons/findByName/${name}`),

  getAll: (): Promise<AxiosResponse<PersonSummary[]>> => api.get('/persons/getAll'),

  getAllMap: (): Promise<AxiosResponse<PersonsMap>> => api.get('/persons/getAllMap'),

  getTreeRootById: (id: EntityId): Promise<AxiosResponse<PersonTreeRoot>> => api.get(`/persons/getTreeRootById/${id}`),
};
