def check_eligibility(scheme, user_profile):

    reasons = []
    information_needed = []
    has_mismatch = False

    age = user_profile.get("age")
    income = user_profile.get("income")
    state = user_profile.get("state")
    occupation = user_profile.get("occupation")
    gender = user_profile.get("gender")
    category = user_profile.get("category")

    eligibility_text = scheme.get("eligibility", "").lower()
    target_group = scheme.get("target_group", "").lower()

    # --------------------------------
    # AGE CHECK
    # --------------------------------

    if age is not None:

        if "18-40" in eligibility_text or "18 to 40" in eligibility_text:

            if 18 <= age <= 40:
                reasons.append(
                    "Age matches the stated 18-40 requirement."
                )
            else:
                has_mismatch = True
                reasons.append(
                    "Age does not match the stated 18-40 requirement."
                )

        else:
            information_needed.append(
                "No specific age requirement could be determined."
            )

    else:
        information_needed.append(
            "Age is required for verification."
        )

    # --------------------------------
    # OCCUPATION CHECK
    # --------------------------------

    if occupation:

        occupation_lower = occupation.lower()

        if "farmer" in target_group or "farmer" in eligibility_text:

            if "farmer" in occupation_lower:
                reasons.append(
                    "Occupation matches the farmer-related target group."
                )
            else:
                has_mismatch = True
                reasons.append(
                    "The scheme targets farmers, but the user's occupation "
                    "does not match."
                )

        else:
            information_needed.append(
                "Occupation is not a determining condition in the "
                "available scheme information."
            )

    else:
        information_needed.append(
            "Occupation is required for verification."
        )

    # --------------------------------
    # INCOME CHECK
    # --------------------------------

    if income is not None:

        if "3 lakh" in eligibility_text:

            if income <= 300000:
                reasons.append(
                    "Income is within the stated Rs. 3 lakh limit."
                )
            else:
                has_mismatch = True
                reasons.append(
                    "Income is above the stated Rs. 3 lakh limit."
                )

        else:
            information_needed.append(
                "Income is not being used as a direct eligibility "
                "condition from the available scheme information."
            )

    else:
        information_needed.append(
            "Income was not provided."
        )

    # --------------------------------
    # GENDER / CATEGORY CHECK
    # --------------------------------

    requires_special_group = (
        "women" in target_group
        or "women" in eligibility_text
        or "sc/st" in eligibility_text
    )

    if requires_special_group:

        if gender or category:

            gender_match = (
                gender
                and "women" in eligibility_text
                and gender.lower() == "female"
            )

            category_match = (
                category
                and "sc/st" in eligibility_text
                and category.lower() in ["sc", "st"]
            )

            if gender_match:
                reasons.append(
                    "Gender matches the stated women-entrepreneur condition."
                )

            elif category_match:
                reasons.append(
                    "Category matches the stated SC/ST condition."
                )

            else:
                has_mismatch = True
                reasons.append(
                    "The user's gender/category does not match the "
                    "stated target-group condition."
                )

        else:
            information_needed.append(
                "Gender or category information is required."
            )

    # --------------------------------
    # STATE CHECK
    # --------------------------------

    if state:
        reasons.append(
            "State information has been provided."
        )
    else:
        information_needed.append(
            "State information is required for verification."
        )

    # --------------------------------
    # LANDHOLDING CHECK
    # --------------------------------

    if "landholding" in eligibility_text:

        information_needed.append(
            "Landholding and farmer records must be verified."
        )

    # --------------------------------
    # FINAL STATUS
    # --------------------------------

    if has_mismatch:

        status = "Not Eligible"

    elif information_needed:

        status = "Potentially Eligible"

    elif reasons:

        status = "Likely Matches Criteria"

    else:

        status = "More Information Needed"

    return {
        "status": status,
        "reasons": reasons,
        "information_needed": information_needed
    }