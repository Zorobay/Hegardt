package se.hegardt.helper

import groovy.transform.CompileStatic

import java.text.Normalizer

@CompileStatic
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
        List<String> searchTokens = search.trim().split(/\s+/).collect { String str -> normalize(str) }
        return searchTokens.every { token -> fuzzedName.contains(token) }
    }

}
