import os

"""
Searcharr
Sonarr, Radarr & Readarr Telegram Bot
By Todd Roberts
https://github.com/toddrob99/searcharr
"""

# Searcharr Bot
searcharr_password = os.getenv('SEARCHARR_PASSWORD', '')  # Used to authenticate as a regular user to add series/movies
searcharr_admin_password = os.getenv('SEARCHARR_ADMIN_PASSWORD', '')  # Used to authenticate as admin to manage users
searcharr_language = os.getenv('SEARCHARR_LANGUAGE', 'en-us')  # yml file in the lang folder
searcharr_start_command_aliases = os.getenv('SEARCHARR_START_COMMAND_ALIASES', 'start').split(',')  # Override /start command
searcharr_help_command_aliases = os.getenv('SEARCHARR_HELP_COMMAND_ALIASES', 'help').split(',')  # Override /help command
searcharr_users_command_aliases = os.getenv('SEARCHARR_USERS_COMMAND_ALIASES', 'users').split(',')  # Override /users command

# Telegram
tgram_token = os.getenv('TGRAM_TOKEN', '')

# Sonarr
sonarr_enabled = os.getenv('SONARR_ENABLED', 'True').lower() == 'true'
sonarr_url = os.getenv('SONARR_URL', '')  # http://192.168.0.100:8989
sonarr_api_key = os.getenv('SONARR_API_KEY', '')
sonarr_quality_profile_id = os.getenv('SONARR_QUALITY_PROFILE_ID', 'HD - 720p/1080p').split(',')  # can be name or id value - include multiple to allow the user to choose
sonarr_add_monitored = os.getenv('SONARR_ADD_MONITORED', 'True').lower() == 'true'
sonarr_search_on_add = os.getenv('SONARR_SEARCH_ON_ADD', 'True').lower() == 'true'
sonarr_tag_with_username = os.getenv('SONARR_TAG_WITH_USERNAME', 'True').lower() == 'true'
sonarr_forced_tags = os.getenv('SONARR_FORCED_TAGS', '').split(',')  # e.g. ["searcharr", "friends-and-family"] - leave empty for none
sonarr_allow_user_to_select_tags = os.getenv('SONARR_ALLOW_USER_TO_SELECT_TAGS', 'True').lower() == 'true'
sonarr_user_selectable_tags = os.getenv('SONARR_USER_SELECTABLE_TAGS', '').split(',')  # e.g. ["custom-tag-1", "custom-tag-2"] - leave empty to let user choose from all tags in Sonarr
sonarr_series_command_aliases = os.getenv('SONARR_SERIES_COMMAND_ALIASES', 'series').split(',')  # e.g. ["series", "tv", "t"]
sonarr_series_paths = os.getenv('SONARR_SERIES_PATHS', '').split(',')  # e.g. ["/tv", "/anime"] - can be full path or id value - leave empty to enable all
sonarr_season_monitor_prompt = os.getenv('SONARR_SEASON_MONITOR_PROMPT', 'False').lower() == 'true'  # False - always monitor all seasons; True - prompt user to select from All, First, or Latest season(s)

# Radarr
radarr_enabled = os.getenv('RADARR_ENABLED', 'True').lower() == 'true'
radarr_url = os.getenv('RADARR_URL', '')  # http://192.168.0.100:7878
radarr_api_key = os.getenv('RADARR_API_KEY', '')
radarr_quality_profile_id = os.getenv('RADARR_QUALITY_PROFILE_ID', 'HD - 720p/1080p').split(',')  # can be name or id value - include multiple to allow the user to choose
radarr_add_monitored = os.getenv('RADARR_ADD_MONITORED', 'True').lower() == 'true'
radarr_search_on_add = os.getenv('RADARR_SEARCH_ON_ADD', 'True').lower() == 'true'
radarr_tag_with_username = os.getenv('RADARR_TAG_WITH_USERNAME', 'True').lower() == 'true'
radarr_forced_tags = os.getenv('RADARR_FORCED_TAGS', '').split(',')  # e.g. ["searcharr", "friends-and-family"] - leave empty for none
radarr_allow_user_to_select_tags = os.getenv('RADARR_ALLOW_USER_TO_SELECT_TAGS', 'True').lower() == 'true'
radarr_user_selectable_tags = os.getenv('RADARR_USER_SELECTABLE_TAGS', '').split(',')  # e.g. ["custom-tag-1", "custom-tag-2"] - leave empty to let user choose from all tags in Radarr
radarr_min_availability = os.getenv('RADARR_MIN_AVAILABILITY', 'released')  # options: "announced", "inCinemas", "released"
radarr_movie_command_aliases = os.getenv('RADARR_MOVIE_COMMAND_ALIASES', 'movie').split(',')  # e.g. ["movie", "mv", "m"]
radarr_movie_paths = os.getenv('RADARR_MOVIE_PATHS', '').split(',')  # e.g. ["/movies", "/other-movies"] - can be full path or id value - leave empty to enable all

# Readarr
readarr_enabled = os.getenv('READARR_ENABLED', 'True').lower() == 'true'
readarr_url = os.getenv('READARR_URL', '')  # http://192.168.0.100:8787
readarr_api_key = os.getenv('READARR_API_KEY', '')
readarr_quality_profile_id = os.getenv('READARR_QUALITY_PROFILE_ID', 'eBook,Spoken').split(',')  # can be name or id value - include multiple to allow the user to choose
readarr_metadata_profile_id = os.getenv('READARR_METADATA_PROFILE_ID', 'Standard').split(',')  # can be name or id value - include multiple to allow the user to choose
readarr_add_monitored = os.getenv('READARR_ADD_MONITORED', 'True').lower() == 'true'
readarr_search_on_add = os.getenv('READARR_SEARCH_ON_ADD', 'True').lower() == 'true'
readarr_tag_with_username = os.getenv('READARR_TAG_WITH_USERNAME', 'True').lower() == 'true'
readarr_forced_tags = os.getenv('READARR_FORCED_TAGS', '').split(',')  # e.g. ["searcharr", "friends-and-family"] - leave empty for none
readarr_allow_user_to_select_tags = os.getenv('READARR_ALLOW_USER_TO_SELECT_TAGS', 'True').lower() == 'true'
readarr_user_selectable_tags = os.getenv('READARR_USER_SELECTABLE_TAGS', '').split(',')  # e.g. ["custom-tag-1", "custom-tag-2"] - leave empty to let user choose from all tags in Readarr
readarr_book_command_aliases = os.getenv('READARR_BOOK_COMMAND_ALIASES', 'book').split(',')  # e.g. ["book", "bk", "b"]
readarr_book_paths = os.getenv('READARR_BOOK_PATHS', '').split(',')  # e.g. ["/books", "/other-books"] - can be full path or id value - leave empty to enable all
