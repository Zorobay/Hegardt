import api from './axios';
import type { AxiosResponse } from 'axios';
import type { Person } from '@/types/person.type.ts';

export const personsService = {
  getById: (id: number): Promise<AxiosResponse<Person>> => api.get(`/persons/${id}`),

  getAll: (): Promise<AxiosResponse<Person[]>> => api.get('/persons/getAll'),

  create: (person: Omit<Person, 'id'>): Promise<AxiosResponse<Person>> => api.post('/persons', person),

  update: (id: number, person: Partial<Person>): Promise<AxiosResponse<Person>> => api.put(`/persons/${id}`, person),

  delete: (id: number): Promise<AxiosResponse<void>> => api.delete(`/persons/${id}`),

  findChildren: (id: number): Promise<AxiosResponse<Person[]>> => api.get(`/persons/${id}/children`),
};
