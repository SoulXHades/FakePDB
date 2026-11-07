"""Compatibility helpers for IDAPython API changes."""

import ida_bytes
import ida_ida
import ida_idaapi
import ida_pro


IDA_90_OR_NEWER = ida_pro.IDA_SDK_VERSION >= 900


def get_procname():
    if IDA_90_OR_NEWER:
        return ida_ida.inf_get_procname()
    return ida_idaapi.get_inf_structure().procname


def get_min_ea():
    if IDA_90_OR_NEWER:
        return ida_ida.inf_get_min_ea()
    return ida_idaapi.get_inf_structure().min_ea


def get_max_ea():
    if IDA_90_OR_NEWER:
        return ida_ida.inf_get_max_ea()
    return ida_idaapi.get_inf_structure().max_ea


def is_64bit():
    if IDA_90_OR_NEWER:
        return ida_ida.inf_is_64bit()
    return ida_idaapi.get_inf_structure().is_64bit()


def is_32bit():
    if IDA_90_OR_NEWER:
        return ida_ida.inf_is_32bit_exactly()
    return ida_idaapi.get_inf_structure().is_32bit()


def get_func_calling_convention(func_type_data):
    """Return a function type's calling convention across IDA versions."""
    if IDA_90_OR_NEWER:
        get_cc = getattr(func_type_data, "get_cc", None)
        if get_cc is not None:
            return get_cc()

    return func_type_data.cc


def find_binary(start_ea, end_ea, pattern):
    """Find a pattern after start_ea, matching ida_search.SEARCH_NEXT."""
    if IDA_90_OR_NEWER:
        return ida_bytes.find_bytes(
            pattern,
            start_ea + 1,
            range_end=end_ea,
            flags=ida_bytes.BIN_SEARCH_FORWARD | ida_bytes.BIN_SEARCH_NOSHOW,
            radix=16,
        )

    import ida_search

    return ida_search.find_binary(
        start_ea,
        end_ea,
        pattern,
        16,
        ida_search.SEARCH_DOWN | ida_search.SEARCH_NEXT,
    )
