from .settings_common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# 開発用ロギング設定
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 既存ロガーを無効にする

    # フィルターの設定
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },

    # フォーマッタの設定
    'formatters': {
        'dev': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '\t'.join(['%(asctime)s',  # ログの出力に「/」を挟む・記録時間の出力
                                 '[%(levelname)s]',  # ログレベルの出力
                                 '%(pathname)s(Line:%(lineno)d)',  # パスと行の出力
                                 '%(message)s',  # メッセージの出力
                                 ])
        }
    },

    # ハンドラの設定
    'handlers': {
        'console': {
            'level': 'DEBUG',  # DEBUG以上のレベルを取り扱う
            'filters': ['require_debug_true'],  # require_debug_trueのフィルタを適用
            'class': 'logging.StreamHandler',  # コンソールへ出力するハンドラであると示す
            'formatter': 'dev',  # devフォーマッタを適用
        },
    },

    # ロガーの設定
    'loggers': {

        # djangoが使用するロガー
        'django': {
            'handlers': ['console'],  # consoleハンドラを適用
            'level': 'INFO',
        },

        # このアプリケーションでデバッグログを出力
        'matching': {
            'handlers': ['console'],    # consoleハンドラを適用
            'level': 'DEBUG',
        },
    }
}
