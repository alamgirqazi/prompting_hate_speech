from encoder_lms import prompting

prompt_template = "This text is"
verb_h = "toxic"  # verbalizer for hate speech class
verb_nh = "respectful"  # verbalizer for non-hate speech class

# Models: roberta-base, roberta-large, bert, deberta-base, deberta-large, xlm-roberta
enc_lms = prompting("roberta-base")

# The input can be a dataframe, a text or a list of texts
enc_lms.predict(prompt_template, verb_h, verb_nh, [
                "You seem nice.", "I hope you white devils get skin cancer and die"])
