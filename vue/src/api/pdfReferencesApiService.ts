import api from '@/api/axios.ts';
import type { PdfReference } from '@/types/pdf-references.type.ts';

export const pdfReferencesApiService = {
  getAllReferences: async (): Promise<Map<number, PdfReference[]>> => {
    const res = await api.get<Record<string, PdfReference[]>>('/pdf/getAllReferences');
    return new Map(Object.entries(res.data).map(([key, value]) => [Number(key), value]));
  },
};
