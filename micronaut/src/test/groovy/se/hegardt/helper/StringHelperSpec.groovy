package se.hegardt.helper

import spock.lang.Specification
import spock.lang.Unroll

class StringHelperSpec extends Specification {

    @Unroll
    def 'normalize(#input) returns "#expected"'() {
        expect:
        StringHelper.normalize(input) == expected

        where:
        input                       | expected
        'Erik'                      | 'erik'
        'ERIK'                      | 'erik'
        'Hélen'                     | 'helen'
        'Åke'                       | 'ake'
        'Ångström'                  | 'angstrom'
        'von Döbel'                 | 'vondobel'
        'Sebastian Lechard Hegardt' | 'sebastianlechardhegardt'
        ''                          | ''
        null                        | ''
    }

}
