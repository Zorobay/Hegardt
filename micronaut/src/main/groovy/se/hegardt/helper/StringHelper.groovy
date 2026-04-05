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

}
