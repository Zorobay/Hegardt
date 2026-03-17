ruleset {

    description 'Hegardt CodeNarc Rules'

    // Basics
    ruleset('rulesets/basic.xml')
    ruleset('rulesets/exceptions.xml')
    ruleset('rulesets/imports.xml') {
        NoWildcardImports
    }
    ruleset('rulesets/unused.xml')

    // Naming conventions
    ruleset('rulesets/naming.xml') {
        MethodName { regex = /[a-z][a-zA-Z0-9_]*/ }
        ClassName { regex = /[A-Z][a-zA-Z0-9]*/ }
        FieldName { regex = /[a-z][a-zA-Z0-9_]*/ }
    }

    // Code style
    ruleset('rulesets/convention.xml') {
        exclude 'NoDef'                  // too strict for Groovy
        exclude 'NoDouble'
    }

    ruleset('rulesets/formatting.xml') {
        exclude 'ClassStartsWithBlankLine'
        exclude 'ClassEndsWithBlankLine'
        exclude 'Indentation'            // let EditorConfig handle this
        LineLength { length = 120 }
    }

    // Groovy-specific
    ruleset('rulesets/groovyism.xml')
    ruleset('rulesets/unnecessary.xml') {
        exclude 'UnnecessaryReturnKeyword' // matter of preference
    }

    // Design
    ruleset('rulesets/design.xml') {
        exclude 'BuilderMethodWithSideEffects'
    }
}
