# web config
web_config = {
    'stone_steps': {
        'web_url': 'https://stepstone.de',
        'name': 'stone_steps',
        'search_page': {
            'input_field': '.styled__Wrapper-dme0a5-0 > div:nth-child(2) > input:nth-child(2)',
            'press_enter': True
            },
        'result_page': {
            'results_container': 'html',
            'links': 'a[data-at=job-item-title]',
            'next_page': 'a.PaginationArrowLink-sc-imp866-0:nth-child(3)'
            },
        'job_page': {
            'job_title': '.listing__job-title',
            'company_name': '.at-listing-nav-company-name-link',
            'email': '.js-emailLink',
            'city': '.location-LocationWithCommuteTimeBlock-trigger',
            'posted_by': '.at-listing-nav-company-name-link'
            },
        'accept_cookies': { 'accept': '#ccmgt_explicit_accept' },
        'noti': { 'button': 'button.at-japubox-popover__modal-close' }
    },
    'job_indeed': {
        'web_url': 'https://de.indeed.com',
        'name': 'job_indeed',
        'search_page': {
            'input_field': '#text-input-what',
            'press_enter': True,
            'url_search': False
            },
        'result_page': {
            'results_container': 'html',
            'links': '.resultWithShelf',
            'next_page': '.pagination-list > li:nth-child(6) > a:nth-child(1)'
            },
        'job_page': {
            'job_title': '.icl-u-xs-mb--xs',
            'company_name': '.icl-u-lg-mr--sm',
            'email': '--no_css_found--',
            'city': '.icl-u-textColor--secondary > div:nth-child(2)',
            'posted_by': '.icl-u-lg-mr--sm'
            },
        'accept_cookies': { 'accept': '#onetrust-accept-btn-handler' }
    },
    'job_ware':{
        'web_url': 'https://jobware.de',
        'name': 'job_ware',
        'search_page':{
            'input_field': 'xpath=//*[@id="jw_jobname"]',
            'search_button': 'xpath=//*[@id="jw_submit"]'
        },
        'job_page': {
            'job_title': '.jw-ad-infos > div:nth-child(2) > h1:nth-child(2)',
            'company_name': 'a.tableCell',
            'email': '.js-emailLink',
            'city': 'div.jw-ad-info:nth-child(2) > div:nth-child(1) > span:nth-child(2)',
            'posted_by': 'a.tableCell'
        },
        'result_page': {
            'results_container': 'html',
            'links': '#result > section > div > div > ng-repeat > article > a'
            },
        'next_page_button_1': {
            'next_button': '#result > section > div > div:nth-child(2) > div.subfooter > a',
            'max_clicks': 10
        },
        'accept_cookies': {'accept': 'xpath=//html/body/div/div/div[3]/div[2]/button'}
    },
    'xing':{
        'web_url': 'https://login.xing.com',
        'base_url':'https://xing.com',
        'name': 'xing',
        'login':{
            'email_field': '#username',
            'password_field': '#password',
            'login_button': '#javascript-content > div.GridWrapper-GridWrapper-contentContainer-0b50c4fe > form > button'
        },
        'search_page':{
            'input_field': 'xpath=//*[@id="malt-xing-frame-ui-search-input"]',
            'select_job': 'xpath=//html/body/div[1]/div[2]/div/div[2]/section/div/main/div/div[1]/main/div[1]/nav/a[2]',
            'press_enter': True
        },
        'job_page': {
            'job_title': '#content > div > div.styles-grid-gridContainer-14980092.styles-grid-standardGridContainer-09b92963 > div > div.posting-header-posting-header-postingHeader-fef54565 > div:nth-child(1) > div > div:nth-child(2) > div > div.styles-grid-col-a25af61b.styles-grid-default9-56c10a1f.styles-grid-confined10-30a0fcc4 > h1',
            'company_name': '#content > div > div.styles-grid-gridContainer-14980092.styles-grid-standardGridContainer-09b92963 > div > div.posting-header-posting-header-postingHeader-fef54565 > div:nth-child(1) > div > div:nth-child(2) > div > div.styles-grid-col-a25af61b.styles-grid-default9-56c10a1f.styles-grid-confined10-30a0fcc4 > div > div.info-info-container-c7e5a698 > a > h2',
            'email': 'no-email-found',
            'city': '#content > div > div.styles-grid-gridContainer-14980092.styles-grid-standardGridContainer-09b92963 > div > div.posting-header-posting-header-postingHeader-fef54565 > div.styles-grid-row-41e25446.subheader-subheader-row-7bd25033 > div > ul > li:nth-child(1) > span',
            'posted_by': '#content > div > div.styles-grid-gridContainer-14980092.styles-grid-standardGridContainer-09b92963 > div > div.posting-header-posting-header-postingHeader-fef54565 > div:nth-child(1) > div > div:nth-child(2) > div > div.styles-grid-col-a25af61b.styles-grid-default9-56c10a1f.styles-grid-confined10-30a0fcc4 > div > div.info-info-container-c7e5a698 > a > h2'
        },
        'result_page': {
            'results_container': 'html',
            'links': "article > a"
            },
        'accept_cookies': {'accept': 'xpath=//*[@id="consent-accept-button"]'}
    },
    'jobs':{
        'web_url': 'https://jobs.de',
        'name': 'jobs',
        'search_page':{
            'input_field': 'xpath=//*[@id="Keywords"]',
            'search_button': 'xpath=//*[@id="sbmt"]'
        },
        'job_page': {
            'job_title': 'h2.h3',
            'company_name': '#jdp-data > div.apply-top-anchor.data-display-header > div.data-display-header_content > div > div.data-display-header_info-content.dib-m > div.data-details > span:nth-child(1)',
            'email': 'a.b',
            'city': '#jdp-data > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(2)',
            'posted_by': '#hide-fixed-top > a:nth-child(1)'
        },
        'result_page': {
            'results_container': 'html',
            'links': 'li.data-results-content-parent > a'
            },
        'next_page_button': {
            'next_button': 'xpath=//html/body/div[1]/div/div[1]/main/div[1]/div[2]/div/div/div[1]/div/div[2]/div[3]/div[3]/div/div[2]/button',
            'max_clicks': 20
        },
        'accept_cookies': {'accept': 'xpath=//*[@id="onetrust-accept-btn-handler"]'}
    },
    'ebay':{
        'web_url': 'https://ebay-kleinanzeigen.de/s-jobs/c102',
        'base_url': 'https://ebay-kleinanzeigen.de',
        'name': 'ebay',
        'search_page':{
            'input_field': 'xpath=//*[@id="site-search-query"]',
            'press_enter': True
        },
        'job_page': {
            'job_title': '#viewad-title',
            'company_name': '#viewad-bizteaser--title > a',
            'email': 'no_email_found',
            'city': '#viewad-locality',
            'posted_by': '.text-body-regular-strong'
        },
        'result_page': {
            'results_container': 'html',
            'links': 'li.ad-listitem > article > div > div > h2 > a',
            'next_page': '.pagination-next'
            },
        'accept_cookies': {'accept': 'xpath=//*[@id="gdpr-banner-accept"]'},
        'noti': { 'button': '#site-signin > div > div > a' }
    },
    'arbeitsagentur':{
        'web_url': 'https://arbeitsagentur.de/jobsuche',
        'compare_url': 'https://www.arbeitsagentur.de',
        'name': 'arbeitsagentur',
        'search_page':{
            'input_field': '#was-input',
            'press_enter': True
        },
        'job_page': {
            'job_title': '#jobdetails-titel',
            'company_name': '#jobdetails-kopf-arbeitgeber',
            'email': 'no_email_found',
            'city': '#jobdetails-arbeitsort',
            'posted_by': '#jobdetails-kopf-arbeitgeber'
        },
        'result_page': {
            'results_container': 'html',
            'links': 'a'
            },

        'accept_cookies': {'accept': 'xpath=//*[@id="bahf-cookie-disclaimer-modal"]/div/div/div[3]/button[2]/bahf-i18n'}
    },
    'monster':{
        'web_url': 'https://monster.de',
        'name': 'monster',
        'search_page':{
            
            'input_field': '#gatsby-focus-wrapper > main > section:nth-child(1) > div > div > div > div.search-sectionstyle__IsTabletAndDesktopOnly-sc-1q9muf3-1.hBuWfs > div > div.ds-search-bar > div.sc-gfqkcP.gOsCGI > form > div > div:nth-child(1) > div > div > div.sc-ksdxgE.cqpTfF > input',
            'press_enter': True,
            'url_search': True
        },
        'job_page': {
            'job_title': '.headerstyle__JobViewHeaderTitle-sc-1ijq9nh-5',
            'company_name': '.headerstyle__JobViewHeaderCompany-sc-1ijq9nh-6',
            'email': '.email_link_disabled',
            'city': '.headerstyle__JobViewHeaderLocation-sc-1ijq9nh-4',
            'posted_by': '.headerstyle__JobViewHeaderCompany-sc-1ijq9nh-6'
        },
        'result_page': {
            'results_container': 'html',
            'links': '#card-scroll-container > div > div > div > div > div > article > div > a'
            },
        'scroll': {
            'scroll_container': '#card-scroll-container',
            'max_clicks': 10
        },
        'accept_cookies': {'accept': '#onetrust-accept-btn-handler'},
        'next_page_button': {
            'next_button': '.job-search-resultsstyle__LoadMoreContainer-sc-1wpt60k-1 > button',
            'max_clicks': 5
        }
    },
    'linkdin':{
        'web_url': 'https://linkedin.com/login',
        'name': 'linkdin',
        'base_url': 'https://linkedin.com',
        'login':{
            'email_field': 'xpath=//*[@id="username"]',
            'password_field': 'xpath=//*[@id="password"]',
            'login_button': 'xpath=//*[@id="organic-div"]/form/div[3]/button'
        },
        'search_page':{
            'input_field': "input[name='keywords']",
            'goto_job': 'https://linkedin.com/jobs',
            'press_enter': True
        },
        'job_page': {
            'job_title': '#main-content > section.core-rail > div > section.top-card-layout > div > div.top-card-layout__entity-info-container > div > h1',
            'company_name': '#main-content > section.core-rail > div > section.top-card-layout > div > div.top-card-layout__entity-info-container > div > h4 > div:nth-child(1) > span:nth-child(1) > a',
            'email': '.email_link_disabled',
            'city': '#main-content > section.core-rail > div > section.top-card-layout > div > div.top-card-layout__entity-info-container > div > h4 > div:nth-child(1) > span.topcard__flavor.topcard__flavor--bullet',
            'posted_by': '#main-content > section.core-rail > div > section.top-card-layout > div > div.top-card-layout__entity-info-container > div > h4 > div:nth-child(1) > span:nth-child(1) > a'
        },
        'result_page': {
            'results_container': 'html',
            'links': '.base-card__full-link'
            },
        'scroll': {
            'scroll_container': '#main-content > section.two-pane-serp-page__results-list',
            'max_clicks': 100
        }
    },
    "valmedi": {
    'web_url': 'https://www.valmedi.de',
    "name": "valmedi",
    "search_page": {
      "input_field": "#q_query",
      "search_button": "#q_submit"
    },
    "result_page": {
      "results_container": "html",
      "links": ".box-left > h3 > a"
    },
    'next_page_button_1': {
            'next_button': '#searchResult > div.row.row-buffer-2x > div.col-md-8 > div:nth-child(2) > div > div:nth-child(5) > div > nav > div > div.box-right > div.page-navigation > a.is-right.is-active',
            'max_clicks': 15
        },
    "job_page": {
      "job_title": "body > div.content-block > div.job-header.blue.pb > div > h1",
      "company_name": "body > div.content-block > div.job-header.blue.pb > div > h2",
      "email": "#contacts > div.contact > p > a",
      "city": ".job-address",
      "posted_by": "body > div.content-block > div.job-header.blue.pb > div > h2"
    }
    },
    "kimeta" : {
    'web_url': 'https://www.kimeta.de/',
    "name": "kimeta",
    "search_page": {
      "input_field": 'xpath=//*[@id="search"]',
      "search_button": '//*[@id="__next"]/div[2]/div[1]/div[4]/form/div/span/button'
    },
    "result_page": {
      "results_container": "html",
      "links": '.jsx-38342742 > a'
    },
    "job_page": {
      "job_title": "/html/body/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/h2",
      "company_name": '#__next > div > div.jsx-1337688730 > div.jsx-644048039.jsx-3369145645.split.split-search-kimeta > div.jsx-1618735476.split-right > div.jsx-2994980512.job > div > div.company > div > section:nth-child(1) > h4.jsx-480145727.company-name',
      "email": "no",
      "city": '#__next > div > div.jsx-1337688730 > div.jsx-644048039.jsx-3369145645.split.split-search-kimeta > div.jsx-1618735476.split-right > div.jsx-2994980512.job > div > div.jsx-2275507171.job-header > div.jsx-2113016801.date-and-location.partner > div > h4',
      "posted_by": '#__next > div > div.jsx-1337688730 > div.jsx-644048039.jsx-3369145645.split.split-search-kimeta > div.jsx-1618735476.split-right > div.jsx-2994980512.job > div > div.jsx-2275507171.job-header > div.jsx-2723962254.job-offer-header-ce > h3'
    },
    'noti': { 'button': 'xpath=/html/body/div[1]/div/div[3]/div/div[1]/div[1]/button' }
  },
    'joblift':{
        'web_url': 'https://joblift.de',
        'name': 'joblift',
        'search_page':{
            
            'input_field': '#jobSearchAutocompleteInput',
            'press_enter': True,
            'url_search': False
        },
        'job_page': {
            'job_title': '#jobDetailsTitle',
            'company_name': '#jobDetailsCompany',
            'email': '.email_link_disabled',
            'city': 'none',
            'posted_by': 'none'
        },
        'result_page': {
            'results_container': 'html',
            'links': '.jobOld__title-wrap > a'
            },
        'accept_cookies': {'accept': '#onetrust-accept-btn-handler'},
        'next_page_button': {
            'next_button': '#applicationWrapper > div > div.page-layout__content > div.resultpage > div.flex__MTk4N.flex--dir-row__NTJhN.flex--jc-flex-start__NzA4O.flex--w-nowrap__Nzk2Z.flex--ai-flex-start__ODk1M.lh-md__MjBmN > div.resultpage__serpList.flex-basis-33pct__MzkzO.lh-md__MjBmN > div > div.searchresult__paginator > div > a:nth-child(6) > span',
            'max_clicks': 20
        },
        'noti': {'button' : 'body > div:nth-child(33) > div > div > div > div > div > svg'}
    },
    'stadi':{
        'web_url': 'https://jobs.meinestadt.de',
        'name': 'stadi',
        'search_page':{
            
            'input_field': '#jobautocompletion',
            'press_enter': True,
            'url_search': False
        },
        'job_page': {
            'job_title': '#headline-22',
            'company_name': '#headline-23',
            'email': '.email_link_disabled',
            'city': '#ms-maincontent > div > div > div > div:nth-child(2) > ul > li:nth-child(1) > span',
            'posted_by': '#headline-23'
        },
        'result_page': {
            'results_container': 'html',
            'links': '.o-resultlist__content > ul > li > div > a'
            },
       
        'accept_cookies': {'accept': '#onetrust-accept-btn-handler'},
        'next_page_button_1': {
            'next_button': '#btn--140',
            'max_clicks': 20
        }
    },
    'karriere':{
        'web_url': 'https://jobs.karriere.de/',
        'name': 'karriere',
        'search_page':{
            
            'input_field': '#job_keyword',
            'press_enter': True,
            'url_search': False
        },
        'job_page': {
            'job_title': 'body > div.o-wrapper > div:nth-child(3) > div > div > div.pagelayout > div > div.listing-container.js-listing-container > div > div.col-lg-12.col-xlg-12.print-100-percent.js-listing-container-left > div.listing-content.js-listing-content.listing-content-liquiddesign > div.listing-header.js-listing-header.at-listing-header > div.listing__top-info > div > div.col-xs-12.col-sm-10.col-md-10.col-lg-10.js-print-header > h1',
            'company_name': 'body > div.o-wrapper > div:nth-child(3) > div > div > div.pagelayout > div > div.listing-container.js-listing-container > div > div.col-lg-12.col-xlg-12.print-100-percent.js-listing-container-left > div.listing-content.js-listing-content.listing-content-liquiddesign > div.listing-header.js-listing-header.at-listing-header > div.listing__top-info > div > div.col-xs-12.col-sm-10.col-md-10.col-lg-10.js-print-company-name > h6 > a3',
            'email': '.email_link_disabled',
            'city': '.listing__highlight > span:nth-child(2)',
            'posted_by': 'body > div.o-wrapper > div:nth-child(3) > div > div > div.pagelayout > div > div.listing-container.js-listing-container > div > div.col-lg-12.col-xlg-12.print-100-percent.js-listing-container-left > div.listing-content.js-listing-content.listing-content-liquiddesign > div.listing-header.js-listing-header.at-listing-header > div.listing__top-info > div > div.col-xs-12.col-sm-10.col-md-10.col-lg-10.js-print-company-name > h6 > a3'
        },
        'result_page': {
            'results_container': 'html',
            'links': 'a'
            },
       
        'accept_cookies': {'accept': 'xpath=//*[@id="notice"]/div[3]/div/div[1]/button[2]'},
        
        'noti': {'button' : 'xpath=//*[@id="japubox-popover__modal"]/div/div/div[1]/button/span'}
    },
     'bundesanzeiger':{
        'web_url': 'https://www.bundesanzeiger.de',
        'name': 'bundesanzeiger',
        'search_page':{
            
            'input_field': '#id3',
            'press_enter': True,
            'url_search': False
        },
        'job_page': {
            'job_title': '#content > section > div > div > div > div > div.container.result_container.global-search.detail-view > div.row.back > div.col-md-3 > div',
            'company_name': 'link_disabled',
            'email': '.email_link_disabled',
            'city': 'linked_disable',
            'posted_by': 'link_disable'
        },
        'result_page': {
            'results_container': 'html',
            'links': '.col-md-5 > div > a'
            },
       
        'accept_cookies': {'accept': '#onetrust-accept-btn-handler'},
        'next_page_button_1': {
            'next_button': '#content > section.indent_top_small.indent_bottom_small > div > div > div > div > div.result_pager.bottom > div.pager_wrapper > nav > div > div.right > div.next',
            'max_clicks': 5
        },
         'noti': {'button': '#cc_all'}
    },
     'jobfinder':{
        'web_url': 'https://www.jobfinder.de',
        'name': 'jobfinder',
        'search_page':{
            
            'input_field': '#search_keywords',
            'search_button': '#main > div > div > main > div > div > section > div > div > form > div.search_jobs > div.search_submit > input[type=submit]',
            'url_search': False
        },
         'next_page_button_1': {
            'next_button': '#main > div > div > main > div > div > section > div > div > a',
            'max_clicks': 15
        },
        'job_page': {
            'job_title': '#main > div > div > main > article > div.entry-content-wrapper.clearfix.standard-content > header > h1 > a',
            'company_name': '#main > div > div > main > article > div.entry-content-wrapper.clearfix.standard-content > div.entry-content > div > div.company > p > strong',
            'email': '.email_link_disabled',
            'city': '#main > div > div > main > article > div.entry-content-wrapper.clearfix.standard-content > div.entry-content > div > ul > li.location > a',
            'posted_by': 'link_disable'
        },
        'result_page': {
            'results_container': 'html',
            'links': '.job_listings > li > a'
            },
       
        'accept_cookies': {'accept': '#BorlabsCookieBox > div > div > div > div.cookie-box > div > div > div > p:nth-child(4)'},
  }
}