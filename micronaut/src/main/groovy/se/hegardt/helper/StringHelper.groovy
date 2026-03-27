package se.hegardt.helper

import java.text.Normalizer

class StringHelper {

    static String normalize(String input) {
        if (!input) return ''
        String normalized = Normalizer.normalize(input, Normalizer.Form.NFD)
        return normalized
            .replaceAll(/\p{InCombiningDiacriticalMarks}/, '')
            .replaceAll(/\s/, '')
            .toLowerCase()
    }

    static boolean fuzzyMatch(String fullName, String search) {
        if (!search?.trim()) return true
        String fuzzedName = normalize(fullName)
        List<String> searchTokens = search.trim().split(/\s+/).collect { normalize(it) }
        return searchTokens.every { token -> fuzzedName.contains(token) }
    }

}
