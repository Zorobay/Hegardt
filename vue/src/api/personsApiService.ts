import api from './axios';
import type { AxiosResponse } from 'axios';
import type { Person, PersonsMap, PersonSummary } from '@/types/person.type.ts';

export const personsApiService = {
  getById: (id: number): Promise<AxiosResponse<Person>> => api.get(`/persons/getById/${id}`),

  getCompleteById: (id: number): Promise<AxiosResponse<Person>> => api.get(`/persons/getCompleteById/${id}`),

  findByName: (name: string): Promise<AxiosResponse<Person[]>> => api.get(`/persons/findByName/${name}`),

  getAll: (): Promise<AxiosResponse<PersonSummary[]>> => api.get('/persons/getAll'),

  getAllMap: (): Promise<AxiosResponse<PersonsMap>> => api.get('/persons/getAllMap'),

  create: (person: Omit<Person, 'id'>): Promise<AxiosResponse<Person>> => api.post('/persons', person),

  update: (id: number, person: Partial<Person>): Promise<AxiosResponse<Person>> => api.put(`/persons/${id}`, person),

  delete: (id: number): Promise<AxiosResponse<void>> => api.delete(`/persons/${id}`),

  findChildren: (id: number): Promise<AxiosResponse<Person[]>> => api.get(`/persons/${id}/children`),
};
